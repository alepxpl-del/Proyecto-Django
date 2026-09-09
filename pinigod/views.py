from django.shortcuts import render, get_object_or_404
from pinigod.models import Pintura


def pinigod(request):
    return render(request, 'pinigod/pinigod.html')

def listado_de_pinturas(request):
    pinturas = Pintura.objects.all()
    return render(request, 'pinigod/listado_de_pinturas.html', {'pinturas': pinturas})

def ver_pintura(request, pk):
    pintura= get_object_or_404(Pintura, pk=pk)
    contexto= {
        "pintura": pintura
    }
    return render(request, "pinigod/ver_pintura.html", contexto)