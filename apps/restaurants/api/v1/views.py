# Thirdy Party
from rest_framework import status
from rest_framework.generics import ListCreateAPIView, RetrieveDestroyAPIView
# Owner
from .serializers import RestaurantSerializer
from ...models import Restaurant
from owner_framework.response import EnvelopeResponse


class RestaurantsView(ListCreateAPIView):
    """
        View for get list restaurants and create a restaurant
        endpoint: /v1/restaurants
    """
    serializer_class = RestaurantSerializer
    queryset = Restaurant.objects.all()


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
