from django.urls import path, re_path
import Musicy.views as vw

urlpatterns = [
    path("",vw.rehome),
    path("home/",vw.home,name="home"),
    path("test/",vw.test,name="test"),
    path("cancionero/",vw.cancionero,name="cancionero"),
    path("musicos/",vw.navegador,name="musicos"),
    path("musicos/buscar/",vw.buscarmus),
    path("musicos/cargar/", vw.formulario,name="formulario"),
    path("musicos/listado/",vw.show),
    path("musicos/borrar/(<int:id>)",vw.deletemus,name="delmus"),
    path("musicos/editar/(<int:id>)",vw.editmus,name="edmus"),
    path("blog/",vw.blog.as_view(),name="blog"),
    path("blog/",vw.crearblog.as_view(),name="nuevo"),
    path(r"^blog/(?P<pk>\d+)$)",vw.blogdetalle.as_view(),name="detalle"),
    path(r"blog/(?P<pk>\d+)/editar$)",vw.editarblog.as_view(),name="editar"),
    path(r"blog/(?P<pk>\d+)/borrar$)",vw.eliminarblog.as_view(),name="borrar"),
]
    