from django.shortcuts import render, redirect
from django.conf import settings
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect, response, request
from .models import Marker, Map
import googlemaps
import json


#MAP VIEWS
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
    current_map_number = len(existing_maps)
    a = Map.objects.create(name=f"{username}'s_map_{current_map_number}", author=request.user)
    a.save()
    
    return redirect('maps:viewmap', id=current_map_number)

def viewmap(request, id):
    if request.method == 'POST':
        print("POST")
        map = Map.objects.get(pk=id)
        stops = map.stop.all()
        marker_list = []
        for marker in stops:
            marker_list.append(marker)
        print (marker_list)
        markers = {
            'markers': marker_list,
        }
        response = render(request, 'maps/partials/marker_list.html', markers)
        return response

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



#MARKER MANIPULATION

def add_marker(request):
    data = request.POST
    tagger_id = request.user
    place_id = data['id']
    info = get_place_by_id(place_id)
    map_id = data['map_id']
    a = Marker.objects.create(lat=info['lat'], lng=info['lng'], address=info['address'], tagger=tagger_id)
    a.save()
    print('marker added')
    current_map = Map.objects.get(id=map_id)
    current_map.stop.add(a)
    current_map_marker_list = current_map.stop.all()
    print(current_map_marker_list)
    context = {
        'markers': current_map_marker_list,
    }
    return render(request, 'maps/partials/marker_list.html', context)

def delete_marker(request):
    data = request.POST
    marker_id = data['id']
    marker = Marker.objects.get(id=marker_id)
    marker.delete()
    return render(request, 'maps/map.html')


#GETTERS

def get_marker_by_id(list):
    markers = []
    for id in list:
        marker = Marker.objects.get(pk=id)
        markers.append(marker)
    context = {
        'markers': markers,
    }
    return context

def get_markers_list(current_map):
    map = current_map
    markers = map.stop.all()
    markers_list = []
    for marker in markers:
        markers_list.append(marker.id)
    markers_info = get_marker_by_id(markers_list)
    context = {
        'markers': markers_info,
    }
    return context

def get_place_by_id(place_id):
    place = place_id
    gmaps= googlemaps.Client(key=settings.GOOGLE_MAPS_API_KEY)
    place_result= json.dumps(gmaps.reverse_geocode(place))
    place_result2 = json.loads(place_result)
    lat = place_result2[0]['geometry']['location']['lat']
    lng = place_result2[0]['geometry']['location']['lng']
    re_place = json.dumps(gmaps.reverse_geocode(latlng=(lat, lng)))
    re_place2 = json.loads(re_place)
    data = {
        'lat': lat,
        'lng': lng,
        'address': re_place2[0]['formatted_address'],
    }
    return data

def get_all_users_maps(request):
    user = request.user
    maps = Map.objects.filter(author=user)
    return maps


#geocode

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


#map manipulation

def rename_map(request):
    if request.method == 'GET':
        map_id = request.GET['map_id']
        map = Map.objects.get(pk=map_id)
        print(request.GET)
        print(map.name)
        title_edit_html = f'<div class="input-group m-auto" style="width:25%;"><button type="button" class="btn btn-danger"><svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-x-circle" viewBox="0 0 16 16"><path d="M8 15A7 7 0 1 1 8 1a7 7 0 0 1 0 14zm0 1A8 8 0 1 0 8 0a8 8 0 0 0 0 16z"/><path d="M4.646 4.646a.5.5 0 0 1 .708 0L8 7.293l2.646-2.647a.5.5 0 0 1 .708.708L8.707 8l2.647 2.646a.5.5 0 0 1-.708.708L8 8.707l-2.646 2.647a.5.5 0 0 1-.708-.708L7.293 8 4.646 5.354a.5.5 0 0 1 0-.708z"/></svg></button><input type="text" class="form-control"id="title_edit" name="title_edit" value="{map.name}"/> <button type="button" class="btn btn-secondary"><svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-check-lg" viewBox="0 0 16 16"><path d="M12.736 3.97a.733.733 0 0 1 1.047 0c.286.289.29.756.01 1.05L7.88 12.01a.733.733 0 0 1-1.065.02L3.217 8.384a.757.757 0 0 1 0-1.06.733.733 0 0 1 1.047 0l3.052 3.093 5.4-6.425a.247.247 0 0 1 .02-.022Z"></path></svg></button></div>'
        return HttpResponse(title_edit_html)
    data = request.POST
    map_id = data['map_id']
    map = Map.objects.get(pk=map_id)
    map.name = data['name']
    map.save()
    return HttpResponse('success')



