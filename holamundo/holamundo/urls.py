"""
URL configuration for holamundo project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static


from rescate_perros.views import holamundo, home, perros, ver_perro, lista_perros, ver_perro_api, nuevo_refugio, ver_refugio, editar_refugio, eliminar_refugio, lista_refugios


urlpatterns = [
    path('admin/', admin.site.urls),
    path('hola/', holamundo, name='holamundo'),
    path('', home, name='home'),
    path('lista_perros/ciudad/<str:ciudad>/', lista_perros, name='lista_perros'),
    path('perro/<int:codigo_perro>/', ver_perro, name='detalle_perro'),
    path('perro_api/<int:codigo_perro>/', ver_perro_api, name='detalle_perro_api'),
    
    # URLS de REFUGIOS
    path('refugio/', lista_refugios, name='lista_refugios'),
    path('refugio/<int:codigo_refugio>/', ver_refugio, name='ver_refugio'),
    path('refugio/nuevo/', nuevo_refugio, name='nuevo_refugio'),
    path('refugio/editar/<int:codigo_refugio>/', editar_refugio, name='editar_refugio'),
    path('refugio/eliminar/<int:codigo_refugio>/', eliminar_refugio, name='eliminar_refugio'),

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
