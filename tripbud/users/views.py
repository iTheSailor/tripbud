from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from .forms import CustomUserCreationForm
from django.contrib import messages



# Create your views here.

#signup view
class RegisterationForm(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("signup")
    template_name = "registration/signup.html"


#login view
class LoginForm(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/login.html"



                    

    
