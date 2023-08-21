#urls.py setup for dashboard
from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView
from .views import first
from . import views

app_name = 'dashboard'


urlpatterns = [
    path('', views.first, name='first'),
    path('newpost', views.new_post, name='newpost'),
    path('modal', views.get_modal, name='modal'),
]
