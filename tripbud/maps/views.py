from django.shortcuts import render, redirect
from django.http import HttpResponse
import googlemaps
from googlemaps import convert, Client, maps
from datetime import datetime
import json
import requests
from django.conf import settings

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

def map(request):
    key = settings.GOOGLE_MAPS_API_KEY
    context = {
        'key': key,
    }
    return render(request, 'maps/map.html', context)
    

