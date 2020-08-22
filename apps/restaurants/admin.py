# Django Core
from django.contrib import admin
from django.contrib.gis.admin import OSMGeoAdmin
# Thirdy party
from import_export.admin import ImportExportModelAdmin
# Owner
from .models import Restaurant
from .resources import RestaurantResource


@admin.register(Restaurant)
class AdminRestaurant(ImportExportModelAdmin, OSMGeoAdmin):
    list_display = ['name', 'rating', 'city']
    search_fields = ['name', ]
    resource_class = RestaurantResource
