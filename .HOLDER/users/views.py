from django.shortcuts import render, redirect
from .models import Profile, Relationship
from django.contrib.auth.models import User
import requests
# Create your views here.

class register(request):
