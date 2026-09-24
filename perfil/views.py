from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from perfil.forms import *

def register(request):
    if request.method == "POST":
        form = UsuariosCreateForm(request.POST)
        if form.is_valid():
            user= form.save()
            login(request, user)
            return redirect("usuario_detail")
    else:
        form = UsuariosCreateForm()
    return render(request, "perfil/registro.html", {"form":form})

@login_required
def usuarios_detail(request):
    return render(request, "perfil/usuario_detail.html", {"usuario": request.user})

def modificar_usuario(request):
    if request.method== "POST":
        form = UsuarioChangeForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect("usuarios_detail")
    else:
        form = UsuarioChangeForm(instance=request.user)
    return render(request, "perfil/modificar_usuario.html", {"form": form})