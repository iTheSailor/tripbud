from . views import *
from django.urls import path, include
from maps import views

urlpatterns = [
    path('', views.map, name='map'),
    path('geocode', views.geocode, name='geocode'),
]