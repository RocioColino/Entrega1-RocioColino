from dataclasses import fields
from django import forms
from .models import *

class NuevoDoctor(forms.ModelForm):
    class Meta:
        model=Doctores
        fields='__all__'

class NuevaPeluqueria(forms.ModelForm):
    class Meta:
        model=Peluquerias
        fields='__all__'

class NuevoRestaurante(forms.ModelForm):
    class Meta:
        model=Restaurantes
        fields='__all__'