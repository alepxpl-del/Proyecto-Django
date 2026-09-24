from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from perfil.models import Usuarios

class UsuariosCreateForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Usuarios
        fields = ("username", "email")

class UsuarioChangeForm(UserChangeForm):
    class Meta:
        model = Usuarios
        fields = ("avatar", "pais", "direccion", "fecha_de_nacimiento", "first_name", "last_name", "password")
        widgets = {
            "avatar": forms.ClearableFileInput(attrs={"class": "form-control"}),
            "pais": forms.TextInput(attrs={"class": "form-control"}),
            "direccion": forms.TextInput(attrs={"class": "form-control"}),
            "fecha_de_nacimiento": forms.DateInput(attrs={"class": "form-control"}),
            "first_name": forms.TextInput(attrs={"class": "form-control"}),
            "last_name": forms.TextInput(attrs={"class": "form-control"}),
            "password": forms.PasswordInput(attrs={"class": "form-control"})
            }