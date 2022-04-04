from django.urls import path
from django.contrib.auth.views import LogoutView
import Musicy.views as vw

urlpatterns = [
    path("inicio/",vw.inicio,name="inicio"),
    path("",vw.reinicio),
    path("cancionero/",vw.cancionero,name="cancionero"),
    path("musicos/",vw.musico,name="musico"),
    path("musicos/buscar/",vw.buscarmusico),
    path("musicos/cargar/", vw.formulariomusico,name="formulario"),
    path("musicos/busqueda/",vw.busquedamusico, name="buscar"),
    path("musicos/borrar/(<int:id>)",vw.borrarmusico,name="delmus"),
    path("musicos/editar/(<int:id>)",vw.editarmusico,name="edmus"),
    path("blog/",vw.blog.as_view(),name="blog"),
    path("blog/nuevo",vw.crearblog.as_view(),name="nuevo"),
    path("blog/(<pk>))",vw.detalleblog.as_view(),name="detalle"),
    path("blog/(<pk>)/editar)",vw.editarblog.as_view(),name="editar"),
    path("blog/(<pk>)/borrar)",vw.eliminarblog.as_view(),name="borrar"),
    path("usuarios/",vw.usuarios,name="login"),
    path("usuarios/ingreso/",vw.loginusuarios),
    path("usuarios/registro/",vw.registrousuarios),
    path("usuarios/logout",LogoutView.as_view(template_name="Usuarios"),name="logout"),
    path("usuarios/editar",vw.editarusuarios,name="usuario"),
    
]
    