from django.contrib import admin
from django.urls import path,include
import Musicy.views as vw

urlpatterns = [
    path("", vw.rehome),    
    path('admin/', admin.site.urls),
    path("musicy/", include("Musicy.urls"))
]