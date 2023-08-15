from django.shortcuts import render, redirect, get_object_or_404
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
    prev_map = get_all_users_maps(request)
    if prev_map:
        for map in get_all_users_maps(request):
            existing_maps.append(map.name)
        current_map_number = len(existing_maps)
        a = Map.objects.create(name=f"{username}'s_map_{current_map_number}", author=request.user)
        a.save()
        return redirect('maps:viewmap', id=current_map_number)
    fledgling_map = Map.objects.create(name=f"welcome, and safe travels, {username}", author=request.user)
    fledgling_map.save()
    return redirect('maps:viewmap', id=fledgling_map.id)

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
    if maps:
        return maps
    return None


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

def rename_map(request, map_id=''):
    map = Map.objects.get(pk=map_id)
    
    if request.method == 'GET':
        print('Into the title change view 1/2')
        print(request.GET)
        print(map.name)
        title_edit_html = '<form id="titlespot" class="input-group m-auto"  hx-swap="outerHTML" style="width:25%;"><button type="button" class="btn btn-danger" hx-target="#titlespot" hx-put="/maps/rename_map/{}"><svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-x-circle" viewBox="0 0 16 16"><path d="M8 15A7 7 0 1 1 8 1a7 7 0 0 1 0 14zm0 1A8 8 0 1 0 8 0a8 8 0 0 0 0 16z"/><path d="M4.646 4.646a.5.5 0 0 1 .708 0L8 7.293l2.646-2.647a.5.5 0 0 1 .708.708L8.707 8l2.647 2.646a.5.5 0 0 1-.708.708L8 8.707l-2.646 2.647a.5.5 0 0 1-.708-.708L7.293 8 4.646 5.354a.5.5 0 0 1 0-.708z"/></svg></button><input type="text" class="form-control" id="title_edit" name="title_edit" value="" placeholder="{}" /><button type="submit" class="btn btn-secondary" hx-target="#titlespot" hx-post="/maps/rename_map/{}"  {}><svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-check-lg" viewBox="0 0 16 16"><path d="M12.736 3.97a.733.733 0 0 1 1.047 0c.286.289.29.756.01 1.05L7.88 12.01a.733.733 0 0 1-1.065.02L3.217 8.384a.757.757 0 0 1 0-1.06.733.733 0 0 1 1.047 0l3.052 3.093 5.4-6.425a.247.247 0 0 1 .02-.022Z"></path></svg></button></form>'.format(map.pk, 'edit map name...',map.pk,'hx-vals=\'{"mykey" : "orzo"}\'')
        print(map.id)
        return HttpResponse(title_edit_html)
    
    
    if request.method == 'PUT':
        print('Into the title change view 2/2')
        data = request.POST
        print(data)
        print(len(data))
        print('| | | =============================>')
        print(' |||   PUT  |||')
        print('| | | =============================>')
        if len(data) < 1:
            print('canceling title change')
            print(map)
            title = '<div id="titlespot" >    <h1>{}   <button type="button"class="btn btn-secondary" id="editbutton" hx-get="/maps/rename_map/{}" hx-target="#titlespot" hx-swap="outerHTML" {}>      <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-pencil-square" viewBox="0 0 16 16"><path d="M15.502 1.94a.5.5 0 0 1 0 .706L14.459 3.69l-2-2L13.502.646a.5.5 0 0 1 .707 0l1.293 1.293zm-1.75 2.456-2-2L4.939 9.21a.5.5 0 0 0-.121.196l-.805 2.414a.25.25 0 0 0 .316.316l2.414-.805a.5.5 0 0 0 .196-.12l6.813-6.814z"></path><path fill-rule="evenodd" d="M1 13.5A1.5 1.5 0 0 0 2.5 15h11a1.5 1.5 0 0 0 1.5-1.5v-6a.5.5 0 0 0-1 0v6a.5.5 0 0 1-.5.5h-11a.5.5 0 0 1-.5-.5v-11a.5.5 0 0 1 .5-.5H9a.5.5 0 0 0 0-1H2.5A1.5 1.5 0 0 0 1 2.5v11z"></path>      </svg>    </h1>  </button>'.format(map.name,map.id, 'hx-vals=\'{"mykey" : "orzo"}\'')
            print(map.pk)
            return HttpResponse(title)
    print("FINALLY AT THE END")
    title = request.POST['title_edit']
    map.name = title
    new_title= '<div id="titlespot" >    <h1>{}   <button type="button"class="btn btn-secondary"  id="editbutton" hx-get="/maps/rename_map/{}" hx-target="#titlespot" hx-swap="outerHTML" {}>      <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-pencil-square" viewBox="0 0 16 16"><path d="M15.502 1.94a.5.5 0 0 1 0 .706L14.459 3.69l-2-2L13.502.646a.5.5 0 0 1 .707 0l1.293 1.293zm-1.75 2.456-2-2L4.939 9.21a.5.5 0 0 0-.121.196l-.805 2.414a.25.25 0 0 0 .316.316l2.414-.805a.5.5 0 0 0 .196-.12l6.813-6.814z"></path><path fill-rule="evenodd" d="M1 13.5A1.5 1.5 0 0 0 2.5 15h11a1.5 1.5 0 0 0 1.5-1.5v-6a.5.5 0 0 0-1 0v6a.5.5 0 0 1-.5.5h-11a.5.5 0 0 1-.5-.5v-11a.5.5 0 0 1 .5-.5H9a.5.5 0 0 0 0-1H2.5A1.5 1.5 0 0 0 1 2.5v11z"></path>      </svg>    </h1>  </button>'.format(map.name,map.id, 'hx-vals=\'{"mykey" : "orzo"}\'')
    return HttpResponse(new_title)

def load_title_partial(request):
    response = render(request, 'maps/partials/title_holder.html')
    return response