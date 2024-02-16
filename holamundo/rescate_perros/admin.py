# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import Perfil_Usuario, Refugio, Perro, AtencionesClinica, Vacuna, Persona, InteresadosEnRescatar


@admin.register(Perfil_Usuario)
class Perfil_UsuarioAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'celular', 'ubicacion', 'foto_usuario')
    list_filter = ('user',)

@admin.register(Refugio)
class RefugioAdmin(admin.ModelAdmin):
    list_display = ('id', 'es_activo', 'nombre', 'direccion', 'descripcion', 'ciudad')


@admin.register(Perro)
class PerroAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'nombre',
        'descripcion',
        'sexo',
        'esterilizado',
        'ficha_perro',
        'fecha_nacimiento',
        'fecha_actualizacion',
        'refugio_actual',
    )
    list_filter = (
        'esterilizado',
        'fecha_nacimiento',
        'fecha_actualizacion',
        'refugio_actual',
    )


@admin.register(AtencionesClinica)
class AtencionesClinicaAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'perro',
        'fecha_atencion',
        'peso',
        'talla',
        'resumen',
        'veterinario',
    )
    list_filter = ('perro', 'fecha_atencion')


@admin.register(Vacuna)
class VacunaAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'fecha_vacunacion',
        'vacuna',
        'certificado',
        'perro',
    )
    list_filter = ('fecha_vacunacion', 'perro')


@admin.register(Persona)
class PersonaAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'nombre',
        'ciudad',
        'telefono',
        'correo',
        'intereses',
        'rol',
    )


@admin.register(InteresadosEnRescatar)
class InteresadosEnRescatarAdmin(admin.ModelAdmin):
    list_display = ('id', 'perro', 'persona')
    list_filter = ('perro', 'persona')