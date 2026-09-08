from django.urls import path
from pinigod.views import pinigod, listado_de_pinturas

urlpatterns = [
    path('', pinigod, name="home"),
    path('pinturas/', listado_de_pinturas, name="listar_pinturas"),
]