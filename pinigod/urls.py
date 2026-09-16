from django.urls import path
from pinigod.views import pinigod, listado_de_pinturas, ver_pintura, crear_pintura, EliminarPintura, EditarPintura

urlpatterns = [
    path('', pinigod, name="home"),
    path('pinturas/', listado_de_pinturas, name="listar_pinturas"),
    path('ver_pintura/<str:pk>', ver_pintura, name="ver_pintura"),
    path('crear_pintura/', crear_pintura, name="crear_pintura"),
    path('eliminar_pintura/<int:pk>/', EliminarPintura.as_view(), name="eliminar_pintura"),
    path('editar_pintura/<int:pk>/', EditarPintura.as_view(), name="editar_pintura"),
]