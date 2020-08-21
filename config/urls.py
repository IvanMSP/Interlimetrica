# Django Core
from django.contrib import admin
from django.urls import path, include
# API Urls
from restaurants.api.v1.urls import restaurants_api_urls

urlpatterns = [
    path('intelimetrica/', admin.site.urls),
    path('api/', include(restaurants_api_urls)),
]
