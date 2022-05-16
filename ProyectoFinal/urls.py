from django.contrib import admin
from django.urls import path,include
import Musicy.views as vw

urlpatterns = [
    path("", vw.reinicio),    
    path('admin/', admin.site.urls),
    path("musicy/", include("Musicy.urls")),
    path("usuarios/", include("Users.urls")),
    path("musicos/", include("Musicos.urls")),
    path("pages/", include("Blog.urls")),
    path("cancion/", include("Cancion.urls")),
    #path(r'^ckeditor/', include('ckeditor_uploader.urls')),
]