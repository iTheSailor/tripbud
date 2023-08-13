from django.db import models
from users.models import CustomUser as User
from django.db.models import ManyToManyField
from googlemaps.maps import static_map, StaticMapMarker, StaticMapPath

# Create your models here.

    
class Marker(models.Model):
    marker_id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
    lat = models.CharField(max_length=200)
    lng = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    tagger = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.address
    
    def get_marker_by_id(self,marker_id):
        marker = marker_id
        return marker
    
    def delete_marker(self,marker_id):
        marker = marker_id
        marker.delete()
        return marker
    



class Map(models.Model):
    map_id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
    name = models.CharField(max_length=200)
    stop = ManyToManyField(Marker)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name