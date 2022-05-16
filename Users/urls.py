from django.urls import path
from django.contrib.auth.views import LogoutView
import Users.views as vw

urlpatterns = [
    path("",vw.usuarios,name="login"),
    path("ingreso/",vw.login_usuarios),
    path("registro/",vw.registro_usuarios),
    path("logout",LogoutView.as_view(template_name="Usuarios"),name="logout"),
    path("editar",vw.editar_usuarios,name="usuario"),
    path("editarpic/",vw.agregar_pic),
]
    