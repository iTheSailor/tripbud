from .models import CustomUser
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib import messages

class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ('username',  'email')

class CustomUserChangeForm(UserChangeForm):
    
        class Meta:
            model = CustomUser
            fields = ('username', 'email')
