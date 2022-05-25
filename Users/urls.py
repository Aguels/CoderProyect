from django.urls import path
from django.contrib.auth.views import LogoutView
import Users.views as vw

urlpatterns = [
    path("",vw.usuarios,name="ingreso"),
    path("ingreso/",vw.login_usuarios, name="login"),
    path("registro/",vw.registro_usuarios, name="registro"),
    path("logout/",LogoutView.as_view(template_name="Users/UsuariosIngreso"),name="logout"),
    path("editar/",vw.editar_usuarios,name="usuario"),
    path("password/",vw.editar_pass),
    path("editarpic/",vw.agregar_avatar),
]
    