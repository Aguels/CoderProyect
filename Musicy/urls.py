from django.urls import path
from django.contrib.auth.views import LogoutView
import Musicy.views as vw

urlpatterns = [
    path("inicio/",vw.inicio,name="inicio"),
    path("",vw.reinicio),
    path("musicos/",vw.musico,name="musico"),
    path("musicos/buscar/",vw.buscar_musico),
    path("musicos/cargar/", vw.formulario_musico,name="formulario"),
    path("musicos/busqueda/",vw.busqueda_musico, name="buscar"),
    path("musicos/borrar/(<int:id>)",vw.borrar_musico,name="delmus"),
    path("musicos/editar/(<int:id>)",vw.editar_musico,name="edmus"),
    path("cancion/",vw.Cancion.as_view(),name="cancion"),
    path("cancion/nuevo",vw.CrearCancion.as_view(),name="nuevo"),
    path("cancion/(<pk>)",vw.DetalleCancion.as_view(),name="detalle"),
    path("cancion/(<pk>)/editar",vw.EditarCancion.as_view(),name="editar"),
    path("cancion/(<pk>)/borrar",vw.EliminarCancion.as_view(),name="borrar"),
    path("usuarios/",vw.usuarios,name="login"),
    path("usuarios/ingreso/",vw.login_usuarios),
    path("usuarios/registro/",vw.registro_usuarios),
    path("usuarios/logout",LogoutView.as_view(template_name="Usuarios"),name="logout"),
    path("usuarios/editar",vw.editar_usuarios,name="usuario"),
    path("pages/",vw.Blog.as_view(),name="blog"),
    path("pages/nuevo",vw.CrearBlog.as_view(),name="nuevob"),
    path("pages/(<pk>)",vw.DetalleBlog.as_view(),name="detalleb"),
    path("pages/(<pk>)/editar",vw.EditarBlog.as_view(),name="editarb"),
    path("pages/(<pk>)/borrar",vw.EliminarBlog.as_view(),name="borrarb"),
    path("about/",vw.about,name="about"),
    path("usuarios/editarpic/",vw.agregar_pic),
    
]
    