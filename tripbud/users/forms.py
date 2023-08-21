from .models import CustomUser as User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib import messages
from django import forms

class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('username',  'email')




class CustomUserChangeForm(UserChangeForm):
    
        class Meta:
            model = User
            fields = ('username', 'email')
