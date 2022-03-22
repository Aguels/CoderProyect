from django.urls import path
from Musicy import views
import Musicy.views as vw

urlpatterns = [
    path("home/",vw.home,name="home"),
    path("test/",vw.test,name="test"),
    path("blog/",vw.blog,name="blog"),
    path("cancionero/",vw.cancionero,name="cancionero"),
    path("registro/",vw.registro,name="registro"),
    path("form/", vw.formulario,name="Formulario"),
    path("navegador/",vw.navegador,name="Buscar"),
    path("loading/",vw.buscar),
    
]
    