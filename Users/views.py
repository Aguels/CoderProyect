from django.shortcuts import render
from Users import forms as f
import django.contrib.auth as ca
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
import Users.models as mod

def usuarios(request):
    return render(request,"Users/Usuarios.html")

def login_usuarios(request):
    if request.method == "POST":
        ingreso = f.Login(request, data=request.POST)
        if ingreso.is_valid():
            usuario = ingreso.cleaned_data.get("username")
            contraseña = ingreso.cleaned_data.get("password")
            user = ca.authenticate(username=usuario, password=contraseña)
            if user is not None:
                ca.login(request, user)
                return render(request, "Musicy/Inicio.html", {"mensaje":f"Bienvenido {user.first_name}"})
            else:
                return render(request, "Musicy/Inicio.html", {"mensaje":"Error: Datos incorrectos."})
        else:
            return render(request,"Musicy/Inicio.html",{"mensaje":"Error: Datos incorrectos."})    
    else:
        ingreso = f.Login()
    return render(request,"Users/UsuariosIngreso.html",{"ingreso":ingreso})

def registro_usuarios(request):
    if request.method == "POST":
        registro = f.Registro(request.POST)
        if registro.is_valid():
            username = registro.cleaned_data["username"]
            registro.save()
            return render(request,"Musicy/Inicio.html",{"mensaje":"Usuario registrado correctamente."})
        else:
            return render(request,"Musicy/Inicio.html",{"mensaje":"Error en los datos ingresados."})
    else:
        registro = f.Registro()
    return render(request,"Users/UsuariosRegistro.html",{"registro":registro})

@login_required
def editar_usuarios(request):
    usuario = request.user
    if request.method == "POST":
        editform = f.EditUser(request.POST)
        if editform.is_valid():
            datos = editform.cleaned_data
            usuario.email = datos["email"]
            usuario.first_name = datos["first_name"]
            usuario.last_name = datos["last_name"]
            usuario.save()
            return render(request, "Musicy/Inicio.html", {"mensaje":"Los datos se han actualizado exitosamente."})
    else:
        editform = f.EditUser(initial={"email":usuario.email,"first_name":usuario.first_name,"last_name":usuario.last_name})
    return render(request, "Users/UsuariosEditar.html",{"formulario":editform,"usuario":usuario})

@login_required
def editar_pass(request):
    usuario = request.user
    if request.method == "POST":
        editform = f.EditPass(usuario,request.POST)
        if editform.is_valid():
            datos = editform.cleaned_data
            usuario.password1 = datos["new_password1"]
            usuario.password2 = datos["new_password2"]
            editform.save()
            return render(request, "Musicy/Inicio.html", {"mensaje":"La contraseña se ha actualizado exitosamente."})
        else:
            return render(request, "Musicy/Inicio.html", {"mensaje":"Error interno."})
    else:
        editform = f.EditPass(usuario,request.POST)
    return render(request, "Users/UsuariosPass.html",{"formulario":editform,"usuario":usuario})


@login_required
def agregar_pic(request):
    usuario = request.user
    if request.method == "POST":
        formularioPic = f.CargarPic(request.POST,request.FILES)
        if formularioPic.is_valid():
            usuariox = User.objects.get(username=usuario)
            Pic = mod.Avatar(user=usuariox, imagen=formularioPic.cleaned_data["imagen"])
            Pic.save()
            return render(request, "Users/UsuariosPic.html", {"mensaje":"La imagen se ha actualizado exitosamente."})
    else:
        formularioPic = f.CargarPic()
    return render(request, "Users/UsuariosPic.html",{"formularioPic":formularioPic,"usuario":usuario})

