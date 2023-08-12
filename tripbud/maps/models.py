from django.db import models
from users.models import CustomUser as User
from django.db.models import ManyToManyField
from googlemaps.maps import static_map, StaticMapMarker, StaticMapPath

# Create your models here.
class markers(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    zipcode = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    lat = models.CharField(max_length=200)
    lng = models.CharField(max_length=200)
    postal_code = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    
class maps(models.Model):
    name = models.CharField(max_length=200)
    stop = ManyToManyField(markers)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    