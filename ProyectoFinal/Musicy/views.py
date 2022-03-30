from django.shortcuts import render
from django.template import loader, context
from django.http import HttpResponse
from Musicy import forms as f
import Musicy.models as mod
from django.shortcuts import redirect
import django.views.generic as dv


def inicio(request):
    dict = {}
    plantilla = loader.get_template("Inicio.html")
    doc = plantilla.render(dict)
    return HttpResponse(doc)

def reinicio(request):
    response = redirect('/musicy/inicio/')
    return response

def cancionero(request):
    dict = {}
    plantilla = loader.get_template("Cancionero.html")
    doc = plantilla.render(dict)
    return HttpResponse(doc)

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