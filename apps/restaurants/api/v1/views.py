# Django Core
from django.contrib.gis.geos import fromstr
from django.contrib.gis.measure import D
from django.db.models import Avg
from django.db.models.aggregates import StdDev
# Thirdy Party
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView, RetrieveDestroyAPIView
# Owner
from .serializers import RestaurantSerializer
from ...models import Restaurant
from owner_framework.response import EnvelopeResponse, EnvelopeErrorResponse
from reusable.constants import NULL_VALUE


class RestaurantsView(ListCreateAPIView):
    """
        View for get list restaurants and create a restaurant
        endpoint: /v1/restaurants
    """
    serializer_class = RestaurantSerializer
    queryset = Restaurant.objects.all().order_by('name')


class RestaurantsDetailView(RetrieveDestroyAPIView):
    """
        View for restaurant detail and delete
        endpoint: /v1/restaurants/<str:id>
    """
    lookup_field = "id"
    serializer_class = RestaurantSerializer
    queryset = Restaurant.objects.all()
    
    def destroy(self, request, *args, **kwargs):
        obj = self.get_object()
        obj.delete()
        return EnvelopeResponse("Restaurant Remove", status=status.HTTP_200_OK)


class StadisticsView(APIView):
    """
        View for Stadistics Restaurants
        endpoint: /v1/restaurants/stadistics
        queryparams:
            latitude
            longitud
            radius
    """
    def get(self, request):
        lat = request.GET.get('latitude', None)
        lng = request.GET.get('longitud', None)
        radius = request.GET.get('radius', None)
        if lat not in NULL_VALUE and lng not in NULL_VALUE and radius not in NULL_VALUE:
            try:
                point = fromstr(f'POINT({lng} {lat})', srid=4326)
                restaurants = Restaurant.objects.filter(location__distance_lte=(point, D(m=radius)))
                rest_count = restaurants.count()
                avg_rating = restaurants.aggregate(avg=Avg('rating'))
                std_rating = restaurants.aggregate(std=StdDev('rating'))
                data = dict(count=rest_count, avg=avg_rating['avg'], std=std_rating['std'])
                return EnvelopeResponse(data, status=status.HTTP_200_OK)
            except Exception:
                return EnvelopeErrorResponse("Params Not Valid", status=status.HTTP_400_BAD_REQUEST)
        return EnvelopeErrorResponse("Missing query params", status=status.HTTP_400_BAD_REQUEST)


