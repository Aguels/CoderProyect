from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from Musicy import forms as f
import Musicy.models as mod
from django.shortcuts import redirect
import django.views.generic as dv
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


class MyView(LoginRequiredMixin, View):
    login_url = '/usuarios/'
    redirect_field_name = 'redirect_to'

def inicio(request):
    return render(request,"Inicio.html")

def reinicio(request):
    return redirect('/musicy/inicio/')

def musico(request):
    musicos = mod.Musician.objects.all()
    return render(request, "Musico/Musico.html", {"Músicos":musicos})

def buscar_musico(request):
    if request.GET["Rol"]:
        rol = request.GET["Rol"]
        ret = mod.Musician.objects.filter(rol__icontains=rol)
        return render(request, "Musico/MusicoResultado.html", {"ret":ret, "rol": rol})
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
    return render(request, "Musico/MusicoFormulario.html", {"Form":Form})

def busqueda_musico(request):
    return render(request, "Musico/MusicoBuscador.html")

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
    return render(request, "Musico/MusicoEditar.html",{"Formed":Formed,"id":id})

class Cancion(dv.ListView):
    model = mod.Song
    template_name = "Cancion/Cancion.html"

class DetalleCancion(dv.DetailView):
    model = mod.Song
    template_name = "Cancion/CancionDetalle.html"

class CrearCancion(LoginRequiredMixin,dv.CreateView):
    model = mod.Song
    success_url = "/musicy/cancion/"
    fields = ["nombre","tono","acordes","letra","link"]
    template_name = "Cancion/CancionFormulario.html"

class EditarCancion(LoginRequiredMixin,dv.UpdateView):
    model = mod.Song
    success_url = "/musicy/cancion/"
    fields = ["nombre","tono","acordes","letra","link"]
    template_name = "Cancion/CancionFormulario.html"

class EliminarCancion(LoginRequiredMixin,dv.DeleteView):
    model = mod.Song
    success_url = "/musicy/cancion/"
    template_name = "Cancion/CancionBorrar.html"

class Blog(dv.ListView):
    model = mod.BlogEntry
    template_name = "Blog/Blog.html"

class DetalleBlog(dv.DetailView):
    model = mod.BlogEntry
    template_name = "Blog/BlogDetalle.html"

class CrearBlog(LoginRequiredMixin,dv.CreateView):
    model = mod.BlogEntry
    success_url = "/musicy/pages/"
    fields = ["titulo","subtitulo","cuerpo"]
    template_name = "Blog/BlogFormulario.html"
    def form_valid(self,form):
        form.instance.autor = self.request.user
        return super().form_valid(form)

class EditarBlog(LoginRequiredMixin,dv.UpdateView):
    model = mod.BlogEntry
    success_url = "/musicy/pages/"
    fields = ["titulo","subtitulo","cuerpo"]
    template_name = "Blog/BlogFormulario.html"

class EliminarBlog(LoginRequiredMixin,dv.DeleteView):
    model = mod.BlogEntry
    success_url = "/musicy/pages/"
    template_name = "Blog/BlogBorrar.html"

def about(request):
    return render(request,"About.html")