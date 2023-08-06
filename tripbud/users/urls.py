from django.urls import path
from .views import RegisterationForm

urlpatterns = [
    path("signup/", RegisterationForm.as_view(), name="signup"),
]