from django.urls import path
import Blog.views as vw

urlpatterns = [
    path("",vw.Blog.as_view(),name="blog"),
    path("nuevo",vw.CrearBlog.as_view(),name="nuevob"),
    path("(<pk>)",vw.DetalleBlog.as_view(),name="detalleb"),
    path("(<pk>)/editar",vw.EditarBlog.as_view(),name="editarb"),
    path("(<pk>)/borrar",vw.EliminarBlog.as_view(),name="borrarb"),
]
    