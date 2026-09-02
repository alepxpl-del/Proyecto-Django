from django.urls import path
from pinigod.views import pinigod, listado_de_pinturas

urlpatterns = [
    path('', pinigod),
    path('pinturas/', listado_de_pinturas)
]