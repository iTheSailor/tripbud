from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import generic
from .forms import CustomUserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from users.models import CustomUser as User
from django.contrib.auth import authenticate, login, logout
import requests
from django.contrib.sessions.models import Session



class RegisterationForm(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"

    def form_valid(self, form):
        messages.success(self.request, "Account created successfully")
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.error(self.request, "Account not created")
        return super().form_invalid(form)
    
# def register(request):
#     if request.method == "POST":
#         form = CustomUserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             print("form is valid")
#             return redirect("login")
#         else:
#             print("form is not valid")
#             form = CustomUserCreationForm()
#             return render(request, "registration/signup.html", {"form": form})

# # Create your views here.
# def profile(request):
#     request.session['user_id'] = request.user.id
#     print(request.session['user_id'])
#     return render(request, 'users/profile.html')


from .forms import SignUpForm

def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            print("form is valid")
            user = form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password')
            print("username is: ", username)
            #sign up user and log them in
            login(request, user)

            return redirect('home')
        messages.error(request, "Account not created")
    else:
        form = SignUpForm()

    # return render(request, '/registration/signup.html', {'form': form})
    return render(request, 'registration/signup.html', {'form': form})



