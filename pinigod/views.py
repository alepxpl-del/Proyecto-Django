from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Max
from pinigod.models import Pintura
from pinigod.forms import PinturaForm


def pinigod(request):
    return render(request, 'pinigod/pinigod.html')

def listado_de_pinturas(request):
    nombre = request.GET.get("nombre")
    pinturas = Pintura.objects.all()
    if nombre is not None:
        pinturas = pinturas.filter(nombre__icontains=nombre)
    return render(request, 'pinigod/listado_de_pinturas.html', {'pinturas': pinturas})

def ver_pintura(request, pk):
    pintura= get_object_or_404(Pintura, pk=pk)
    contexto= {
        "pintura": pintura
    }
    return render(request, "pinigod/ver_pintura.html", contexto)

def crear_pintura(request):
    if request.method == "POST":
        form = PinturaForm(request.POST)
        if form.is_valid():
            pintura= form.save(commit=False)
            max_num = Pintura.objects.aggregate(Max('nro_pintura'))['nro_pintura__max']
            pintura.nro_pintura = (max_num or 0) + 1
            pintura.save()
            return redirect("listar_pinturas")
    else:
        form = PinturaForm()

    return render(request, "pinigod/crear_pintura.html", {"form": form})