from django import forms
from .models import *

class RefugioForm(forms.ModelForm):
    class Meta:
        model = Refugio
        fields = ['nombre', 'direccion', 'descripcion', 'ciudad', 'tipo']
        