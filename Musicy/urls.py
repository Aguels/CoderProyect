from django.urls import path
from django.contrib.auth.views import LogoutView
import Musicy.views as vw

urlpatterns = [
    path("",vw.inicio,name="inicio"),
    path("about/",vw.about,name="about"),
]
    