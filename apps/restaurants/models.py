# Django Core
import uuid
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.gis.db import models
from django.contrib.gis.geos import fromstr
# Owner
from reusable.constants import BLANK, REQUIRED


class Restaurant(models.Model):
    """
        Restaurant Model
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    rating = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(4)],
        default=0
    )
    name = models.CharField(max_length=150, **REQUIRED)
    site = models.URLField()
    email = models.EmailField()
    phone = models.CharField(max_length=20, **BLANK)
    street = models.CharField(max_length=150, **BLANK)
    city = models.CharField(max_length=150, **BLANK)
    state = models.CharField(max_length=150, **BLANK)
    lat = models.DecimalField(max_digits=18, decimal_places=13)
    lng = models.DecimalField(max_digits=18, decimal_places=13)
    location = models.PointField(**BLANK)

    def save(self, *args, **kwargs):
        self.location = fromstr(f'POINT({self.lng} {self.lat})', srid=4326)
        super(Restaurant, self).save(*args, **kwargs)

    def __str__(self):
        return self.name
