from django.urls import path
from pinigod.views import pinigod, listado_de_pinturas, ver_pintura, crear_pintura, EliminarPintura, EditarPintura, iniciar_sesion, registro
from django.contrib.auth.views import LogoutView
urlpatterns = [
    path('', pinigod, name="home"),
    path('pinturas/', listado_de_pinturas, name="listar_pinturas"),
    path('ver_pintura/<str:pk>', ver_pintura, name="ver_pintura"),
    path('crear_pintura/', crear_pintura, name="crear_pintura"),
    path('eliminar_pintura/<int:pk>/', EliminarPintura.as_view(), name="eliminar_pintura"),
    path('editar_pintura/<int:pk>/', EditarPintura.as_view(), name="editar_pintura"),
    path('iniciar_sesion/', iniciar_sesion, name="iniciar_sesion"),
    path('cerrar_sesion/', LogoutView.as_view(template_name='pinigod/cerrar_sesion.html'), name="cerrar_sesion"),
    path('registro/', registro, name="registro"),
]