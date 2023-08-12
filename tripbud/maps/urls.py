from . views import *
from django.urls import path, include, re_path
from maps import views

app_name = 'maps'

urlpatterns = [
    path('viewmap', views.viewmap, name='viewmap'),
    path('geocode', views.geocode, name='geocode'),
]