# Django Core
from django.contrib import admin
# Owner
from .models import Restaurant


@admin.register(Restaurant)
class AdminRestaurant(admin.ModelAdmin):
    pass
