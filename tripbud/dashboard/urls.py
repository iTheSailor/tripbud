#urls.py setup for dashboard
from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView
from .views import DashboardView
from . import views

app_name = 'dashboard'


urlpatterns = [
    
    path('', DashboardView.as_view(), name='dashboard'),
    path('content/<int:post_id>', views.post_detail, name='post_detail'),
    path('content/<int:post_id>/edit', views.edit_post, name='post_edit'),
    path('content/<int:post_id>/like', views.like_post, name='like_post'),
    path('content/<int:post_id>/delete', views.delete_post, name='post_delete'),
    path('content/<int:post_id>/detail', views.post_detail, name='post_detail'),
    path('content/create_post', views.create_post, name='create_post'),
    path('content/add_comment', views.add_comment, name='add_comment'),
]
