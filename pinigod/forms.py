from django import forms
from pinigod.models import Pintura

class PinturaForm(forms.ModelForm):
    class Meta:
        model = Pintura
        fields = ("nombre", "autor", "descripcion")