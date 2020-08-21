# Django Core
from django.urls import path
# Owner
from .views import RestaurantsView, RestaurantsDetailView

restaurants_api_urls = [
    path("v1/restaurants", RestaurantsView.as_view(), name="restaurants"),
    path("v1/restaurants/<str:id>", RestaurantsDetailView.as_view(), name="restaurants-detail"),
]
