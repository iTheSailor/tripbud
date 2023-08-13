from . views import *
from django.urls import path, include, re_path
from maps import views

app_name = 'maps'

urlpatterns = [
    path('initmap', views.initmap, name='initmap'),
    path('geocode', views.geocode, name='geocode'),
    path('add_marker', views.add_marker, name='add_marker'),
    path('delete_marker/<int:id>', views.delete_marker, name='delete_marker'),
    # path('get_marker', views.get_markers, name='get_marker'),
    path('newmap', views.newmap, name='newmap'),
    path('<int:id>', views.viewmap, name='viewmap'),
    path('get_markers_list', views.get_markers_list, name='get_markers_list'),
]