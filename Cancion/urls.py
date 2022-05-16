from django.urls import path
import Cancion.views as vw

urlpatterns = [
    path("",vw.Cancion.as_view(),name="cancion"),
    path("nuevo",vw.CrearCancion.as_view(),name="nuevo"),
    path("(<pk>)",vw.DetalleCancion.as_view(),name="detalle"),
    path("(<pk>)/editar",vw.EditarCancion.as_view(),name="editar"),
    path("(<pk>)/borrar",vw.EliminarCancion.as_view(),name="borrar"),
]
    