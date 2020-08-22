# Django Core
from django.urls import path
# Owner
from .views import RestaurantsView, RestaurantsDetailView, StadisticsView

restaurants_api_urls = [
    path("v1/restaurants", RestaurantsView.as_view(), name="restaurants"),
    path("v1/restaurants/<str:id>", RestaurantsDetailView.as_view(), name="restaurants-detail"),
    path("v1/stadistics", StadisticsView.as_view(), name="stadistics"),
]
