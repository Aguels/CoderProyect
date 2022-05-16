from django.urls import path
import Musicos.views as vw

urlpatterns = [
    path("",vw.musico,name="musico"),
    path("buscar/",vw.buscar_musico),
    path("cargar/", vw.formulario_musico,name="formulario"),
    path("busqueda/",vw.busqueda_musico, name="buscar"),
    path("borrar/(<int:id>)",vw.borrar_musico,name="delmus"),
    path("editar/(<int:id>)",vw.editar_musico,name="edmus"),    
]
    