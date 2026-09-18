from django import forms
from pinigod.models import Pintura
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class PinturaForm(forms.ModelForm):
    class Meta:
        model = Pintura
        fields = ("nombre", "autor", "descripcion")

class MiFormularioDeCreacion(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput,)
    password2 = forms.CharField(label='Confirmar contraseña', widget=forms.PasswordInput,)

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'email')
        help_texts = {key: '' for key in fields }