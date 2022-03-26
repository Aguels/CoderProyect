from django.urls import path
import Musicy.views as vw

urlpatterns = [
    path("home/",vw.home,name="home"),
    path("test/",vw.test,name="test"),
    path("blog/",vw.blog,name="blog"),
    path("cancionero/",vw.cancionero,name="cancionero"),
    path("registro/",vw.registro),
    path("form/", vw.formulario,name="formulario"),
    path("navegador/",vw.navegador,name="registro"),
    path("loading/",vw.buscar),
    
]
    