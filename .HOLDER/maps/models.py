from django.db import models
from django.db.models.fields.related import ForeignKey
from django.contrib.auth.models import User
from googlemaps.maps import static_map, StaticMapMarker, StaticMapPath
# Create your models here.

class Marker(models.Model):
    marker_id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
    lat = models.CharField(max_length=6)
    lng = models.CharField(max_length=6)
    address = models.CharField(max_length=200)
    tagger = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.address
    

    
class Map(models.Model):
    map_id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
    name = models.CharField(max_length=200)
    stop = models.ManyToManyField(Marker)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
    def get_map_by_id(self,map_id):
        _map = map_id
        return _map
    
    def get_all_maps_by_author(self,author):
        maps = Map.objects.filter(author=author)
        return maps
    
    def delete_map(self,map_id):
        _map = map_id
        _map.delete()
        return _map
    
    def rename_map(self,map_id,new_name):
        _map = map_id
        _map.name = new_name
        _map.save()
        return _map
    
    def add_marker(self,map_id,marker_id):
        _map = map_id
        marker = marker_id
        _map.stop.add(marker)
        _map.save()
        return _map
    
    def remove_marker(self,map_id,marker_id):
        _map = map_id
        marker = marker_id
        _map.stop.remove(marker)
        _map.save()
        return _map
    
    def get_all_maps_by_author(self,author):
        maps = Map.objects.filter(author=author)
        return maps
    
