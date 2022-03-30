from django.contrib import admin
from django.urls import path,include
import Musicy.views as vw

urlpatterns = [
    path("", vw.reinicio),    
    path('admin/', admin.site.urls),
    path("musicy/", include("Musicy.urls"))
]