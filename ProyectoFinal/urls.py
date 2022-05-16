from django.contrib import admin
from django.urls import path,include
import Musicy.views as vw
from django.conf.urls.static import static

urlpatterns = [
    path("", vw.reinicio),    
    path('admin/', admin.site.urls),
    path("musicy/", include("Musicy.urls")),
    path("users/", include("Users.urls")),
    path(r'^ckeditor/', include('ckeditor_uploader.urls')),
]