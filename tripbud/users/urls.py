from django.urls import path
from .views import RegisterationForm, signup_view
from . import views

urlpatterns = [
    path("signup/", signup_view, name="signup"),
    # path("register/", views.register, name="register"),
    # path("profile/", views.profile, name="profile"),

]