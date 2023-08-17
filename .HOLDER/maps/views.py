from django.shortcuts import render, redirect
from django.conf import settings
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect, response, request
from .models import Marker, Map
from googlemaps import geolocation
import json
# Create your views here.

KEY = settings.GOOGLE_MAPS_API_KEY

def initmap(request):
    location = geolocation.geolocate(KEY)
    return render(request, 'maps/initmap.html', location)

def getmap(request):
    _map = Map.get_map_by_id(request.GET.get('map_id'))
    markers = _map.stop.all()
    context = {
        'map': _map,
        'markers': markers,
    }
    return render(request, 'maps/getmap.html', context)

def get_all_user_maps(request):
    user = request.user
    maps = Map.get_all_maps_by_author(user)
    return maps


def newmap(request):
    username = request.user
    existing_maps = []
    prev_map = get_all_user_maps(request)
    if prev_map:
        for map in get_all_user_maps(request):
            existing_maps.append(map.name)
        current_map_number = len(existing_maps)
        a = Map.create_map(f"{username}'s_map_{current_map_number}", request.user)
        a.save()
        return redirect('maps:getmap', id=current_map_number)
    fledgling_map = Map.create_map(f"welcome, and safe travels, {username}", request.user)
    fledgling_map.save()
    return redirect('maps:getmap', id=fledgling_map.id)

def viewmap(request, id):
    if request.method == 'POST':
        _map = Map.get_map_by_id(id)
        stops = _map.stop.all()
        marker_list = []
        for marker in stops:
            marker_list.append(marker)
        markers = {
            'markers': marker_list,
        }
        response = render(request, 'maps/partials/marker_list.html', markers)
        return response
    _map = Map.get_map_by_id(id)
    stops = _map.stop.all()
    key = KEY
    context = {
        'map_id': _map.id,
        'key': key,
        'map': _map,
        'markers': stops,
    }
    load_partial(request)
    return render(request, 'maps/map.html',  context)

def load_partial(request):
    response = render(request, 'maps/partials/marker_list.html')
    return response


    
