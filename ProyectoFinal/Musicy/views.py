from django.shortcuts import render
from django.template import loader, context
from django.http import HttpResponse
from Musicy import forms as f
import Musicy.models as mod
from django.shortcuts import redirect
import django.views.generic as dv
import django.contrib.auth.forms as djf
import django.contrib.auth as ca
from django.contrib.auth.decorators import login_required


def inicio(request):
    return render(request,"Inicio.html")

def reinicio(request):
    return redirect('/musicy/inicio/')

def cancionero(request):
    return HttpResponse("Work in progress")

def musico(request):

    musicos = mod.Musician.objects.all()
    return render(request, "Musico.html", {"Músicos":musicos})

def buscarmusico(request):
    if request.GET["Rol"]:
        rol = request.GET["Rol"]
        ret = mod.Musician.objects.filter(rol__icontains=rol)
        return render(request, "MusicoResultado.html", {"ret":ret, "rol": rol})
    else:
        respuesta = "No enviaste datos."
        return HttpResponse(respuesta)

def formulariomusico(request):
    if request.method == "POST":
        Form = f.mus(request.POST)
        print(Form)
        if Form.is_valid:
            dato = Form.cleaned_data
            Up = mod.Musician(nombre=dato["Nombre"], rol=dato["Rol"])
            Up.save()
            return redirect("/musicy/musicos/")
    else:
        Form = f.mus()
    return render(request, "MusicoFormulario.html", {"Form":Form})

def busquedamusico(request):
    return render(request, "MusicoBuscador.html")

def borrarmusico(request, id):
    musico = mod.Musician.objects.get(id=id)
    musico.delete()
    return redirect("/musicy/musicos/")

def editarmusico(request,id):
    musico = mod.Musician.objects.get(id=id)
    if request.method == "POST":
        Formed = f.mus(request.POST)
        print(Formed)

        if Formed.is_valid:
            datos = Formed.cleaned_data
            musico.nombre = datos["Nombre"]
            musico.rol = datos["Rol"]
            musico.save()
            return redirect("/musicy/musicos/")
    else:
        Formed = f.mus(initial= {"Nombre" : musico.nombre, "Rol" : musico.rol})
    return render(request, "MusicoEditar.html",{"Formed":Formed,"id":id})

class blog(dv.ListView):
    model = mod.BlogEntry
    template_name = "Blog.html"

class detalleblog(dv.DetailView):
    model = mod.BlogEntry
    template_name = "BlogDetalle.html"

class crearblog(dv.CreateView):
    model = mod.BlogEntry
    success_url = "/musicy/blog/"
    fields = ["titulo","cuerpo"]
    template_name = "BlogFormulario.html"

class editarblog(dv.UpdateView):
    model = mod.BlogEntry
    success_url = "/musicy/blog/"
    fields = ["titulo","cuerpo"]
    template_name = "BlogFormulario.html"

class eliminarblog(dv.DeleteView):
    model = mod.BlogEntry
    success_url = "/musicy/blog/"
    template_name = "BlogBorrar.html"

def usuarios(request):
    ingreso = f.login()
    registro = f.registro()
    return render(request,"Usuarios.html", {"ingreso":ingreso, "registro":registro,})

def loginusuarios(request):
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

def registrousuarios(request):
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
def editarusuarios(request):
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

