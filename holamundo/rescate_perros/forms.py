from django import forms
from .models import *

class RefugioForm(forms.ModelForm):
    class Meta:
        model = Refugio
        fields = ['nombre', 'direccion', 'descripcion', 'ciudad', 'tipo', 'documento', 'foto']
        

class Perfil_Usuario_Form(forms.ModelForm):
    class Meta:
        model = Perfil_Usuario
        fields = ['celular', 'ubicacion', 'foto_usuario']