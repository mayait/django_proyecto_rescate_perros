# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import Postulante, Personal, Refugio, Perro, AtencionesClinica, Vacuna, Persona, InteresadosEnRescatar, Country, City, Category, Product, Order, OrderLine


@admin.register(Postulante)
class PostulanteAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'department')
    list_filter = ('user',)


@admin.register(Personal)
class PersonalAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'department')
    list_filter = ('user',)


@admin.register(Refugio)
class RefugioAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'nombre',
        'direccion',
        'tipo',
        'descripcion',
        'ciudad',
        'fecha_actualizacion',
        'es_activo',
        'documento',
    )
    list_filter = ('fecha_actualizacion', 'es_activo')


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
        'foto',
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


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'country', 'state', 'postal_code')
    raw_id_fields = ('country',)
    search_fields = ('name',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'sub_category')
    search_fields = ('name',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'product_id', 'name', 'category')
    raw_id_fields = ('category',)
    search_fields = ('name',)


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'order_id',
        'order_date',
        'ship_date',
        'ship_mode',
        'customer_id',
        'customer_name',
        'segment',
        'city',
        'region',
    )
    list_filter = ('order_date', 'ship_date')
    raw_id_fields = ('city',)


@admin.register(OrderLine)
class OrderLineAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'order',
        'product',
        'sales',
        'quantity',
        'discount',
        'profit',
    )
    raw_id_fields = ('order', 'product')
