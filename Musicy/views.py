from django.shortcuts import render
from django.template import loader, context
from django.http import HttpResponse
from django.views import View
from Musicy import forms as f
import Musicy.models as mod
from django.shortcuts import redirect
import django.views.generic as dv
import django.contrib.auth.forms as djf
import django.contrib.auth as ca
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User


class MyView(LoginRequiredMixin, View):
    login_url = '/usuarios/'
    redirect_field_name = 'redirect_to'

def inicio(request):
    return render(request,"Inicio.html")

def reinicio(request):
    return redirect('/musicy/inicio/')

def musico(request):
    musicos = mod.Musician.objects.all()
    return render(request, "Musico.html", {"Músicos":musicos})

def buscar_musico(request):
    if request.GET["Rol"]:
        rol = request.GET["Rol"]
        ret = mod.Musician.objects.filter(rol__icontains=rol)
        return render(request, "MusicoResultado.html", {"ret":ret, "rol": rol})
    else:
        respuesta = "No enviaste datos."
        return HttpResponse(respuesta)

@login_required
def formulario_musico(request):
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

def busqueda_musico(request):
    return render(request, "MusicoBuscador.html")

@login_required
def borrar_musico(request, id):
    musico = mod.Musician.objects.get(id=id)
    musico.delete()
    return redirect("/musicy/musicos/")

@login_required
def editar_musico(request,id):
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

class Cancion(dv.ListView):
    model = mod.Song
    template_name = "Cancion.html"

class DetalleCancion(dv.DetailView):
    model = mod.Song
    template_name = "CancionDetalle.html"

class CrearCancion(LoginRequiredMixin,dv.CreateView):
    model = mod.Song
    success_url = "/musicy/cancion/"
    fields = ["nombre","tono","acordes","letra","link"]
    template_name = "CancionFormulario.html"

class EditarCancion(LoginRequiredMixin,dv.UpdateView):
    model = mod.Song
    success_url = "/musicy/cancion/"
    fields = ["nombre","tono","acordes","letra","link"]
    template_name = "CancionFormulario.html"

class EliminarCancion(LoginRequiredMixin,dv.DeleteView):
    model = mod.Song
    success_url = "/musicy/cancion/"
    template_name = "CancionBorrar.html"

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

class Blog(dv.ListView):
    model = mod.BlogEntry
    template_name = "Blog.html"

class DetalleBlog(dv.DetailView):
    model = mod.BlogEntry
    template_name = "BlogDetalle.html"

class CrearBlog(LoginRequiredMixin,dv.CreateView):
    model = mod.BlogEntry
    success_url = "/musicy/pages/"
    fields = ["titulo","subtitulo","cuerpo"]
    template_name = "BlogFormulario.html"
    def form_valid(self,form):
        form.instance.autor = self.request.user
        return super().form_valid(form)

class EditarBlog(LoginRequiredMixin,dv.UpdateView):
    model = mod.BlogEntry
    success_url = "/musicy/pages/"
    fields = ["titulo","subtitulo","cuerpo"]
    template_name = "BlogFormulario.html"

class EliminarBlog(LoginRequiredMixin,dv.DeleteView):
    model = mod.BlogEntry
    success_url = "/musicy/pages/"
    template_name = "BlogBorrar.html"

def about(request):
    return render(request,"About.html")

#def buscarPic(user):
#    return mod.Pic.objects.filter(user=user)[0].imagen.url
#{"Pic":buscarPic(request.user)}

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