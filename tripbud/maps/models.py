from django.db import models
from googlemaps.maps import static_map, StaticMapMarker, StaticMapPath

# Create your models here.
class markers(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    zipcode = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    latitude = models.CharField(max_length=200)
    longitude = models.CharField(max_length=200)
    altitude = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    


    