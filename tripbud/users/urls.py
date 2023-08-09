from django.urls import path
from .views import RegisterationForm

urlpatterns = [
    path("signup/", RegisterationForm.as_view(), name="signup"),
    path("login/", RegisterationForm.as_view(), name="login")
]