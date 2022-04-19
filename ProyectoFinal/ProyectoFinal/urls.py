from django.contrib import admin
from django.urls import path,include
import Musicy.views as vw
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", vw.reinicio),    
    path('admin/', admin.site.urls),
    path("musicy/", include("Musicy.urls"))
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)