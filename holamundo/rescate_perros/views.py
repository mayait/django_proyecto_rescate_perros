from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response

from rest_framework import serializers

from django.contrib.auth.decorators import login_required

# importar formularios
from .forms import RefugioForm, Perfil_Usuario_Form


# Importar modelos
from .models import Perro, Refugio, Perfil_Usuario

@login_required
def ver_perfil_usuario(request):
    c = {}
    if hasattr(request.user, 'perfil'):
        perfil = request.user.perfil
    else:
        perfil = Perfil_Usuario(user=request.user)
    if request.method == 'POST':
        form = Perfil_Usuario_Form(request.POST, request.FILES, instance=perfil)
        if form.is_valid():
            form.save()
    else:
        form = Perfil_Usuario_Form(instance=perfil)
    c['form'] = form
    c['refugio']= perfil

    return render(request, 'perfil_usuario.html', c)


def nuevo_refugio(request):
    contenido = {}
    if request.method == 'POST':
        contenido['form'] = RefugioForm(
                        request.POST or None,
                        request.FILES or None,
                        )
        if contenido['form'].is_valid():
            contenido['form'].save()
            return redirect(contenido['form'].instance.get_absolute_url())
        
    contenido['instancia_refugio'] = Refugio()
    contenido['form'] = RefugioForm(
        request.POST or None,
        request.FILES or None,
        instance = contenido['instancia_refugio']
    )
    return render(request, 'formulario_refugio.html', contenido)

@login_required
def editar_refugio(request, codigo_refugio):
    c = {}
    refugio = get_object_or_404(Refugio, pk=codigo_refugio)
    if request.method == 'POST':
        form = RefugioForm(request.POST, request.FILES, instance=refugio)
        if form.is_valid():
            form.save()
            return redirect(refugio.get_absolute_url())
    else:
        form = RefugioForm(instance=refugio)
    c['form'] = form
    c['refugio']= refugio
    return render(request, 'formulario_refugio.html', c)

def eliminar_refugio(request, codigo_refugio):
    c = {}
    c['refugio'] =  get_object_or_404(Refugio, pk=codigo_refugio)
    c['refugio'].es_activo = False
    c['refugio'].save()
    return redirect('lista_refugios')


def ver_refugio(request, codigo_refugio):
    c = {}
    c['refugio'] =  get_object_or_404(Refugio, pk=codigo_refugio)
    return render(request, 'refugio.html', c)

def lista_refugios(request):
    c = {}
    c['refugios'] = Refugio.objects.filter(es_activo=True)
    return render(request, 'lista_refugios.html', c)



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
    if hasattr(request.user, 'perfil'):
        perfil = request.user.perfil
        return redirect('ver_perfil_usuario')
    
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