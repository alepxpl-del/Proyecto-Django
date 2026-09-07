from django.shortcuts import render
from pinigod.models import Pintura

def pinigod(request):
    return render(request, 'pinigod/pinigod.html')

def listado_de_pinturas(request):
    pinturas = Pintura.objects.all()
    return render(request, 'pinigod/listado_de_pinturas.html', {'pinturas': pinturas})