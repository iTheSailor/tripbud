from .models import Marker, Map
from django import forms

class MarkerForm(forms.ModelForm):
    class Meta:
        model = Marker
        fields = ['lat', 'lng', 'address', 'tagger']

class MapForm(forms.ModelForm):
    class Meta:
        model = Map
        fields = ['name', 'stop', 'author']