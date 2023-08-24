from .models import CustomUser as User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib import messages
from django import forms

class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder': 'Username'}, ))
    email = forms.EmailField(required=True, widget=forms.TextInput(attrs={'placeholder': 'Email'}))
    password1 = forms.CharField(required=True, widget=forms.PasswordInput(attrs={'placeholder': 'Password'}, ))
    password2 = forms.CharField(required=True, widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password'}, ))

    class Meta:
        model = User
        fields = ('username',  'email')




class CustomUserChangeForm(UserChangeForm):
    
        class Meta:
            model = User
            fields = ('username', 'email')



from django import forms
from .models import CustomUser 
class SignUpForm(forms.ModelForm):
    username = forms.CharField(max_length=30, required=True, help_text="Required.") 
    email = forms.EmailField(max_length=254, help_text="Required. Enter a valid email address.")
    password = forms.CharField(widget=forms.PasswordInput, min_length=8, help_text="Minimum 8 characters.")
    password2 = forms.CharField(widget=forms.PasswordInput, min_length=8, help_text="Minimum 8 characters.")
    
    error_messages = {
            'password_mismatch': ("The two password fields didn't match."),
            'required': ("This field is required."),
            'invalid': ("Enter a valid value."),
            'unique': ("A user with that username already exists."),
        }
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
    

