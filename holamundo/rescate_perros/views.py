from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse

from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

# Paginador
from django.core.paginator import Paginator


# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response

from rest_framework import serializers

from .utils import *

# importar formularios
from .forms import RefugioForm


# Importar modelos
from .models import *

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
    c['color'] = request.COOKIES.get('color', 'ninguno')
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
    template = 'index.html'
    c = {
        'titulo': 'ESTA ES TU CASA',
        'mensaje': 'Este es un mensaje desde la vista home'
    }
    c['contar_frecuencia_palabras'] = contar_frecuencia_palabras('Este es un mensaje de prueba para contar palabras, y otras palabras')
    c['texto_traducido'] = traducir('Hola mundo')

    if hasattr(request.user, 'postulante'):
        c['tiene_postulante'] = True
    if hasattr(request.user, 'personal'):
        c['tiene_personal'] = True

    response = render(request, template, c)
    response.set_cookie('color', 'azul', max_age=90000)
    response.set_cookie('tamanio', 'max', max_age=90000)

    return response

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

def import_excel_view(request):
    import_excel_to_django()
    return HttpResponse("Correcto!!!")


def product_list(request):
    products_list = Product.objects.all()
    paginator = Paginator(products_list, 100)  # Mostrar 10 productos por página

    page_number = request.GET.get('page')
    products = paginator.get_page(page_number)

    return render(request, 'lista_productos.html', {'products': products})


class ProductDetailView(DetailView):
    model = Product
    template_name = 'product_detail_view.html'
    context_object_name = 'product'