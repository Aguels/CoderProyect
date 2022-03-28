from django.urls import path
import Musicy.views as vw

urlpatterns = [
    path("",vw.rehome),
    path("home/",vw.home,name="home"),
    path("test/",vw.test,name="test"),
    path("blog/",vw.blog,name="blog"),
    path("cancionero/",vw.cancionero,name="cancionero"),
    path("musicos/",vw.navegador,name="musicos"),
    path("musicos/buscar/",vw.buscarmus),
    path("musicos/cargar/", vw.formulario,name="formulario"),
    path("musicos/listado/",vw.show),
    path("musicos/borrar/(<int:id>)",vw.deletemus,name="delmus"),
]
    