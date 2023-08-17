from django.contrib import admin
from .models import Map, Marker

# Register your models here.
app = 'maps'

admin.site.register(Map)
admin.site.register(Marker)
