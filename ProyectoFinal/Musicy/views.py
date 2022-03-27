from django.shortcuts import render
from django.template import loader, context
from django.http import HttpResponse
from Musicy import forms as f
import Musicy.models as mod
from django.shortcuts import redirect

def home(request):
    dict = {}
    plantilla = loader.get_template("Home.html")
    doc = plantilla.render(dict)
    return HttpResponse(doc)

def test(request):
    dict = {}
    plantilla = loader.get_template("Pater.html")
    doc = plantilla.render(dict)
    return HttpResponse(doc)

def blog(request):
    dict = {}
    plantilla = loader.get_template("Blog.html")
    doc = plantilla.render(dict)
    return HttpResponse(doc)

def cancionero(request):
    dict = {}
    plantilla = loader.get_template("Cancionero.html")
    doc = plantilla.render(dict)
    return HttpResponse(doc)

def registro(request):
    dict = {}
    plantilla = loader.get_template("Registro.html")
    doc = plantilla.render(dict)
    return HttpResponse(doc)

def formulario(request):
    if request.method == "POST":
        Form = f.inputmus(request.POST)
        print(Form)
        if Form.is_valid:
            dato = Form.cleaned_data
            Up = mod.Musician(nombre=dato["Nombre"], rol=dato["Rol"])
            Up.save()

            return redirect("/musicy/musicos/")
    
    else:
        Form = f.inputmus()
    
    return render(request, "Forms.html", {"Form":Form})

def navegador(request):

    return render(request, "Navegador.html")

def buscar(request):
    if request.GET["Rol"]:
        rol = request.GET["Rol"]
        ret = mod.Musician.objects.filter(rol__icontains=rol)
        return render(request, "Resultado.html", {"ret":ret, "rol": rol})

    else:
        respuesta = "No enviaste datos."
        return HttpResponse(respuesta)

def rehome(request):
    response = redirect('/musicy/home/')
    return response

def show(request):
    musicos = mod.Musician.objects.all()
    return render(request, "Listado.html", {"Músicos":musicos})

def deletemus(request, id):
    musico = mod.Musician.objects.get(id=id)
    musico.delete()
    return redirect("/musicy/musicos/listado/")