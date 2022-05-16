from django.shortcuts import render
from django.http import HttpResponse
from Musicos import forms as f
import Musicos.models as mod
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

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
