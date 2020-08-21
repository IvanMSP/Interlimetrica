# Django Core
from django.urls import path
# Owner
from .views import RestaurantsView

restaurants_api_urls = [
    path("v1/restaurants", RestaurantsView.as_view(), name="restaurants"),
    path("v1/restaurants/<str:id>", RestaurantsView.as_view(), name="restaurant-detail"),
]
