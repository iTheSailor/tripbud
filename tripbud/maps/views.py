from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect, response
import googlemaps
from googlemaps import convert, Client, maps, places
from googlemaps.places import PLACES_DETAIL_FIELDS_BASIC, PLACES_FIND_FIELDS_BASIC
from datetime import datetime
import json
import requests
from django.conf import settings
from django.views import generic
from django.urls import reverse_lazy
from .models import Marker, Map
from django.contrib.contenttypes.models import ContentType
from users.models import CustomUser as User


# Create your views here.

def geocode(request):
    gmaps = googlemaps.Client(key=settings.GOOGLE_MAPS_API_KEY)
    loc_result = json.dumps(gmaps.geocode('1600 Amphitheatre Parkway, Mountain View, CA'))
    loc_result2 = json.loads(loc_result)
    latitude = loc_result2[0]['geometry']['location']['lat']
    longitude = loc_result2[0]['geometry']['location']['lng']
    elev_result = json.dumps(gmaps.elevation((latitude, longitude)))
    elev_result2 = json.loads(elev_result)
    elevation = "{:.2f}".format(elev_result2[0]['elevation'])
    context = {
        'lat': latitude,
        'lng': longitude,
        'elev': elevation,
    }
    return render(request, 'maps/geocode.html', context)

def initmap(request):

    key = settings.GOOGLE_MAPS_API_KEY
    context = {
        'key': key,
    }
    return render(request, 'maps/initmap.html', context)


def newmap(request):
    username = request.user
    existing_maps = []
    get_all_users_maps(request)
    for map in get_all_users_maps(request):
        existing_maps.append(map.name)
    current_map_number = len(existing_maps) + 1
    a = Map.objects.create(name=f"{username}'s_map_{current_map_number}", author=request.user)
    a.save()
    
    return redirect('maps:viewmap', id=map_id)

def get_all_users_maps(request):
    user = request.user
    maps = Map.objects.filter(author=user)
    return maps

def viewmap(request, id):
    map = Map.objects.get(pk=id)
    markers = map.stop.all()
    key = settings.GOOGLE_MAPS_API_KEY
    context = {
        'map_id': map.id,
        'key': key,
        'map': map,
        'markers': markers,
    }
    load_partial(request)
    return render(request, 'maps/map.html',  context)

def load_partial(request):
    response = render(request, 'maps/partials/marker_list.html')
    return response

def get_place_by_id(place_id):
    place = place_id
    # print(place)
    key = settings.GOOGLE_MAPS_API_KEY
    gmaps= googlemaps.Client(key=settings.GOOGLE_MAPS_API_KEY)
    place_result= json.dumps(gmaps.reverse_geocode(place))
    place_result2 = json.loads(place_result)
    lat = place_result2[0]['geometry']['location']['lat']
    lng = place_result2[0]['geometry']['location']['lng']
    re_place = json.dumps(gmaps.reverse_geocode(latlng=(lat, lng)))
    re_place2 = json.loads(re_place)
    # print(re_place2[0])
    data = {
        'lat': lat,
        'lng': lng,
        'address': re_place2[0]['formatted_address'],
    }
    return data



current_markers= {}


def add_marker(request):
    # print(request.POST)
    data = request.POST
    tagger_id = request.user
    place_id = data['id']
    info = get_place_by_id(place_id)
    a = Marker.objects.create(lat=info['lat'], lng=info['lng'], address=info['address'], tagger=tagger_id)
    a.save()
    current_map = Map.objects.get(map_id)
    current_map.stop.add(a)
    print('marker added')
    entry = {
        'id': a.id,
        'lat': a.lat,
        'lng': a.lng,
        'address': a.address,
    }
    return redirect(get_markers_list(request))

def get_markers_list(request):
    map = Map.objects.get(id)
    markers = map.stop.all()
    markers_list = []
    for marker in markers:
        markers_list.append(marker.id)
    markers_info = get_marker_by_id(request, markers_list)
    context = {
        'markers': markers_info,
    }
    return render(request, 'maps/partials/marker_list.html', context)


def get_marker_by_id(request, list):
    markers = []
    for id in list:
        marker = Marker.objects.get(pk=id)
        markers.append(marker)
    context = {
        'markers': markers,
    }
    return context





def delete_marker(request):
    data = request.POST
    marker_id = data['id']
    marker = Markers.objects.get(id=marker_id)
    marker.delete()
    return render(request, 'maps/map.html')

# def get_markers(request):
     



    
    

