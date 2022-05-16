from django.shortcuts import render
from Users import forms as f
import django.contrib.auth as ca
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
import Users.models as mod

def usuarios(request):
    ingreso = f.login()
    registro = f.registro()
    return render(request,"Usuarios.html", {"ingreso":ingreso, "registro":registro,})

def login_usuarios(request):
    if request.method == "POST":
        ingreso = f.login(request, data=request.POST)
        if ingreso.is_valid():
            usuario = ingreso.cleaned_data.get("username")
            contraseña = ingreso.cleaned_data.get("password")
            user = ca.authenticate(username=usuario, password=contraseña)
            if user is not None:
                ca.login(request, user)
                return render(request, "Inicio.html", {"mensaje":f"Bienvenido {user.first_name}"})
            else:
                return render(request, "Inicio.html", {"mensaje":"Error: Datos incorrectos."})
        else:
            return render(request,"Inicio.html",{"mensaje":"Error: Datos incorrectos."})    
    else:
        return render(request,"Inicio.html",{"mensaje":"Error en formulario."})

def registro_usuarios(request):
    if request.method == "POST":
        registro = f.registro(request.POST)
        if registro.is_valid():
            username = registro.cleaned_data["username"]
            registro.save()
            return render(request,"Inicio.html",{"mensaje":"Usuario registrado correctamente."})
        else:
            return render(request,"Inicio.html",{"mensaje":"Error en los datos ingresados."})
    else:
        return render(request,"Inicio.html",{"mensaje":"Error HTML."})

@login_required
def editar_usuarios(request):
    usuario = request.user
    if request.method == "POST":
        editform = f.eduser(request.POST)
        if editform.is_valid():
            datos = editform.cleaned_data
            usuario.email = datos["email"]
            usuario.password1 = datos["password1"]
            usuario.password2 = datos["password2"]
            usuario.first_name = datos["first_name"]
            usuario.last_name = datos["last_name"]
            usuario.save()
            return render(request, "Inicio.html", {"mensaje":"Los datos se han actualizado exitosamente."})
    else:
        editform = f.eduser(initial={"email":usuario.email,"first_name":usuario.first_name,"last_name":usuario.last_name})
    return render(request, "UsuariosEditar.html",{"formulario":editform,"usuario":usuario})

@login_required
def agregar_pic(request):
    usuario = request.user
    if request.method == "POST":
        formularioPic = f.cargarPic(request.POST,request.FILES)
        if formularioPic.is_valid():
            usuariox = User.objects.get(username=usuario)
            Pic = mod.Pic(user=usuariox, imagen=formularioPic.cleaned_data["imagen"])
            Pic.save()
            return render(request, "Inicio.html", {"mensaje":"La imagen se ha actualizado exitosamente."})
    else:
        formularioPic = f.cargarPic()
    return render(request, "UsuariosPic.html",{"formularioPic":formularioPic,"usuario":usuario})

