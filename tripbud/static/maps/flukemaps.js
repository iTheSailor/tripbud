var infowindow;

function initMap() {
  var map = new google.maps.Map(
    document.getElementById("map_canvas"), {
      center: new google.maps.LatLng(37.4419, -122.1419),
      zoom: 13,
      mapTypeId: google.maps.MapTypeId.ROADMAP
    });
  var marker = new google.maps.Marker({
    position: map.getCenter(),
    map: map
  });

  infowindow = new google.maps.InfoWindow({
    content: " "
  });

  google.maps.event.addListener(marker, 'click', function() {
    infowindow.setContent('<p>Event Name: ' + this.title + '</p>' +
      '<p>Event Type: ' + this.etype + '</p>' +
      '<p>Cause: ' + this.cause + '</p>' +
      '<p>Date: ' + this.date + '</p>' +
      '<p>Time: ' + this.time + '</p>' +
      '<button onclick="myFunction()">Click me</button>');
    infowindow.open(map, this);
  });
  google.maps.event.trigger(marker, 'click');
}
google.maps.event.addListener(window, "load", initMap);

function myFunction() {
  infowindow.setContent('<div style="background-color: green">' + infowindow.getContent() + "</div>");
}