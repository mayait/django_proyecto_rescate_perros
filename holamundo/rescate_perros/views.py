from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response

from rest_framework import serializers


# Importar modelos
from .models import Perro, Refugio

def ver_perro(request, codigo_perro):
    
    # Query del perro, un perro con el codigo
    perro = Perro.objects.get(pk = codigo_perro)
    
    # creo un diccionario con el objeto
    contenido = {
        'perro' : perro
    }

    template = "ver_perro.html"

    return render(request, template, contenido)

def lista_perros(request, ciudad):
    #perros = Perro.objects.all()
    perros = Perro.objects.filter(refugio_actual__ciudad__iexact=ciudad)
    contenido = {
        'perros' : perros
    }
    template = "lista_perros.html"
    return render(request, template, contenido)

class RefugioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Refugio
        fields = '__all__'

class PerroSerializer(serializers.ModelSerializer):
    refugio_actual = RefugioSerializer()
    class Meta:
        model = Perro
        fields = '__all__'



@api_view()
def ver_perro_api(request, codigo_perro):
    perro = Perro.objects.get(pk=codigo_perro)
    serializer = PerroSerializer(perro)
    return Response(serializer.data)



@api_view()
def holamundo(request):
    perros = [
        {
            'nombre': 'Firulais',
            'edad': 5,
            'raza': 'Pastor Aleman'
        },
        {
            'nombre': 'Rocky',
            'edad': 3,
            'raza': 'Bulldog'
        },
        {
            'nombre': 'Rex',
            'edad': 7,
            'raza': 'Pitbull'
        }
    ]
    return Response(perros)

def home(request):
    template = 'index.html'
    c = {
        'titulo': 'ESTA ES TU CASA',
        'mensaje': 'Este es un mensaje desde la vista home'
    }
    return render(request, template, c)

def perros(request, nombre, edad):
    template = 'perros.html'
    owner = request.GET.get('owner', 'Desconocido')
    comida = request.GET.get('comida', 'nada')
    contenido = {
        'mensaje': f'Este perro tiene {edad} años, el dueño es {owner} y solo come {comida}',
        'titulo': nombre,
        'comida': comida
    }

    print(request.GET)
    
    return render(request, template, contenido)