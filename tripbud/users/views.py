from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from .forms import CustomUserCreationForm
from django.contrib import messages



# Create your views here.

class RegisterationForm(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"


                    

    
# class ProfileView(generic.TemplateView):
#     template_name = "registration/profile.html"

# class EditProfileView(generic.TemplateView):
#     template_name = "registration/edit_profile.html"

    