import Blog.models as mod
import django.views.generic as dv
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View

class MyView(LoginRequiredMixin, View):
    login_url = '/usuarios/'
    redirect_field_name = 'redirect_to'
    
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
