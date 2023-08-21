from django.urls import path
from .views import RegisterationForm
from . import views

urlpatterns = [
    path("signup/", RegisterationForm.as_view(), name="signup"),
    # path("register/", views.register, name="register"),
    # path("profile/", views.profile, name="profile"),

]