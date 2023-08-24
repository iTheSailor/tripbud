#urls.py setup for dashboard
from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView
from .views import DashboardView
from . import views

app_name = 'dashboard'


urlpatterns = [
    path('', DashboardView.as_view(), name='dashboard'),
    path('content/create_post', views.create_post, name='create_post'),
    path('content/add_comment', views.add_comment, name='add_comment'),
]
