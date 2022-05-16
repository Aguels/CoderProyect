import Cancion.models as mod
import django.views.generic as dv
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View

class MyView(LoginRequiredMixin, View):
    login_url = '/usuarios/'
    redirect_field_name = 'redirect_to'

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