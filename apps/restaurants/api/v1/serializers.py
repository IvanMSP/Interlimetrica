# Thirdy Party
from rest_framework import serializers

# Owner
from ...models import Restaurant


class RestaurantSerializer(serializers.ModelSerializer):
    """
        Restaurant Serializer
        Used by: restaurants, restaurants-detail endpoints
    """
    id = serializers.CharField(read_only=True, required=False)
    detail = serializers.HyperlinkedIdentityField(
        read_only=True,
        lookup_field="id",
        view_name="restaurants-detail"
    )

    class Meta:
        model = Restaurant
        fields = (
            "id",
            "rating",
            "name",
            "site",
            "email",
            "phone",
            "street",
            "city",
            "state",
            "lat",
            "lng",
            "detail",
            "location",
        )

