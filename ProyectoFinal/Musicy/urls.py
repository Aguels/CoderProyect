from django.urls import path
from Musicy import views
import Musicy.views as vw

urlpatterns = [
    path("home/",vw.home),
    path("test/",vw.test),
]
