from dataclasses import fields
from django import forms
from .models import *

class NuevoDoctor(forms.ModelForm):
    class Meta:
        model=Doctores
        fields='__all__'