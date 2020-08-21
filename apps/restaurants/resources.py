# Thirdy Party
from import_export import resources
from import_export.fields import Field
# Owner
from .models import Restaurant


class RestaurantResource(resources.ModelResource):

    class Meta:
        model = Restaurant
        fields = (
            'id',
            'rating',
            'name',
            'site',
            'email',
            'phone',
            'street',
            'city',
            'state',
            'lat',
            'lng',
        )

