from django.contrib import admin
from pinigod.models import Pintura
#Metodo 1 para registrar:
#admin.site.register(Pintura)
#Metodo 2 para registrar
@admin.register(Pintura)
class PinturaAdmin(admin.ModelAdmin):
    #Columna visible en el listado de registros.
    list_display= ("nombre", "fecha_de_creacion")
    #Campo que funciona como link para entral al detalle/registro.
    list_display_links= ("nombre",)
    #Habilita la barra de busqueda de registros.
    search_fields= ("nombre", "autor")
    #Agrega el panel lateral de registros.
    list_filter= ("fecha_de_creacion",)
    #Determina el orden de los datos registrados.
    ordering= ("nombre", "autor", "fecha_de_creacion")
    #Fecha visible pero no editable.
    readonly_fields= ("fecha_de_creacion",)
