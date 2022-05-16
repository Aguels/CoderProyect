from django.urls import path
from django.contrib.auth.views import LogoutView
import Users.views as vw

urlpatterns = [
    path("usuarios/",vw.usuarios,name="login"),
    path("usuarios/ingreso/",vw.login_usuarios),
    path("usuarios/registro/",vw.registro_usuarios),
    path("usuarios/logout",LogoutView.as_view(template_name="Usuarios"),name="logout"),
    path("usuarios/editar",vw.editar_usuarios,name="usuario"),
    path("usuarios/editarpic/",vw.agregar_pic),
]
    