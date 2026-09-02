from django.shortcuts import render

def pinigod(request):
    return render(request, 'pinigod/pinigod.html')

def listado_de_pinturas(request):
    pinturas = []
    numeros = list(range(16))
    return render(request, 'pinigod/listado_de_pinturas.html', {'pinturas': pinturas, 'numeros': numeros})