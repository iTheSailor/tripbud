let map, service, marker;
let markers = [];

var infoWindow = new google.maps.InfoWindow();

const bounds = new google.maps.LatLngBounds({
    south: 39,
    west: -76,
    north: 39,
    east: -76,
});


async function initMap(){
    const { Map } = await google.maps.importLibrary('maps');
    map = new Map(document.getElementById("map"), {
        center: { lat: 39, lng: -76 },
        zoom: 8,
    });
    map.addListener("click", (event) => {
        showInfo(event.latLng);
    });
    document.getElementById("show-markers").addEventListener("click", () => {
        showMarkers();
    }
    );
    document.getElementById("clear-markers").addEventListener("click", () => {
        clearMarkers();
    }
    );
    document.getElementById("delete-markers").addEventListener("click", () => {
        deleteMarkers();
    }
    );
    document.getElementById("pan-to-current-location").addEventListener("click", () => {
        panToCurrentLocation();
    }
    );
    document.getElementById("search-location").addEventListener("click", () => {
        finder();
    }
    );
}


function showInfo(latLng) {
    // console.log(latLng);
    geocoder = new google.maps.Geocoder();
    geocoder.geocode(
        { location: latLng },
        (results, status) => {
            if (status === "OK") {
                if (results[0]) {
                    map.setZoom(11);
                    // console.log(results[0]);
                    infoWindow.setContent(
                        '<div id="info-window">' +
                        '<p>Location: ' + results[0].formatted_address + '</p>' +
                        '<p>Latitude: ' + latLng.lat() + '</p>' +
                        '<p>Longitude: ' + latLng.lng() + '</p>' +
                        '<button id="add-location" hx-trigger="click" hx-post="/maps/add_marker" hx-target="#markerslist" onclick="createMarker.addLocation()" method="POST" value='+latLng+'>Add Location</button>' +
                        '<button id="cancel" onclick="createMarker.cancelLocation()">Cancel</button>'
                        + '</div>',
                        );
                    infoWindow.setPosition (latLng);
                    };
                    infoWindow.open(map, this);
                    createMarker(results[0]);
                    
                }
            }
        );
    }

function geolocation(lat, lng){
    geocoder = new google.maps.Geocoder();
    var latlng = new google.maps.LatLng(lat, lng);
    geocoder.geocode({'latLng': latlng}, function(results, status) {
        if (status == google.maps.GeocoderStatus.OK) {
        if (results[1]) {
            var indice=0;
            for (var j=0; j<results.length; j++)
            {
                if (results[j].types[0]=='locality')
                    {
                        indice=j;
                        break;
                    }
            }

            for (var i=0; i<results[j].address_components.length; i++)
            {
                if (results[j].address_components[i].types[0] == "locality") {
                        //this is the object you are looking for
                        city = results[j].address_components[i];
                    }
                if (results[j].address_components[i].types[0] == "administrative_area_level_1") {
                        //this is the object you are looking for
                        region = results[j].address_components[i];
                    }
                if (results[j].address_components[i].types[0] == "country") {
                        //this is the object you are looking for
                        country = results[j].address_components[i];
                    }
            }
            //city data
            location_name = city.long_name + ", " + region.long_name + ", " + country.short_name;
            // console.log(location_name);
            return location_name;
        }
        else {
            location_name = "No results";
            // console.log(location_name);
            return location_name;
        }
    }
});
}



function finder(){
    var input = document.getElementById('searchTextField');
    var request = {
        query: input.value,
        fields: ["name", "geometry"],
    };
    service = new google.maps.places.PlacesService(map);
    service.findPlaceFromQuery(request, (results, status) => {


        if (status === google.maps.places.PlacesServiceStatus.OK && results) {
            map.setCenter(results[0].geometry.location);
            result = results[0].geometry.location
            infoWindow.setContent(
                '<div id="info-window">' +
                '<button id="add-location" onclick="addLocation()" value='+result+'>Add Location</button>' +
                '<button id="cancel" onclick="cancelLocation()">Cancel</button>'
                + '</div>',
                );
            infoWindow.setPosition(results[0].geometry.location);

            infoWindow.open(map, this);    
                  
        }
    });
}




function createMarker(place) {
    marker = new google.maps.Marker({
        map,
        position: place.geometry.location,
        id: place.place_id,
    });
    console.log(place);
    console.log(place.geometry.location.lat());
    console.log(place.geometry.location.lng());
    console.log(place.place_id);

    markers.push(marker);
    console.log(markers);
    function addLocation(){ 
        infoWindow.close();
        const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;

        $.ajax({
            headers: { "X-CSRFToken": csrftoken },
            type: "POST",
            url: "/maps/add_marker",
            data: {
                'id' : place.place_id,
            },
            success: function(data){
                console.log(data);
            }
        });

    }

    createMarker.addLocation = addLocation;
    function cancelLocation(){
        markers[markers.length-1].setMap(null);
        infoWindow.close();
    }

    createMarker.cancelLocation = cancelLocation;

      
}



function setMapOnAll(map) {
    for (var i = 0; i < markers.length; i++) {
      markers[i].setMap(map);
    }
  }

// async function createMarker(place) {

//     if (place.geometry.viewport) {
//         bounds.union(place.geometry.viewport);
//     } else {
//         bounds.extend(place.geometry.location);
//     }
//     var marker = new google.maps.Marker({
//         map,
//         position: place.geometry.location,
//     });
//     markers.push(marker);

// }

function showMarkers() {
    setMapOnAll(map);
}

function clearMarkers() {
    setMapOnAll(null);
}

function deleteMarkers() {
    clearMarkers();
    markers = [];
}


function panToCurrentLocation(){
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(
            (position) => {
                const pos = {
                    lat: position.coords.latitude,
                    lng: position.coords.longitude,
                };
                
                map.setCenter(pos);
                createMarker(pos);
                infoWindow.setContent(
                    "Location found.",
                    );
                infoWindow.setPosition( pos);
                infoWindow.open(map, this);
            },
            () => {
                handleLocationError(true, infoWindow, map.getCenter());
            }
        );
    } else {
        // Browser doesn't support Geolocation
        handleLocationError(false, infoWindow, map.getCenter());
    }
}

function handleLocationError(browserHasGeolocation, infoWindow, pos) {
    infoWindow = new google.maps.InfoWindow();
    infoWindow.setPosition(pos);
    infoWindow.setContent(
        browserHasGeolocation
            ? "Error: The Geolocation service failed."
            : "Error: Your browser doesn't support geolocation."
    );
    infoWindow.open(map, this);
    }