from . views import *
from django.urls import path, include
from maps import views as view

urlpatterns = [
    path('geocode', view.geocode, name='geocode'),
    path('map', view.map, name='map'),
]