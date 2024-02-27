from django.db import models
from django.utils import timezone
from datetime import date
from django.urls import reverse
from django.contrib.auth.models import User


class Postulante(models.Model):
    user = models.OneToOneField(User, related_name='postulante', on_delete=models.CASCADE)
    department = models.CharField(max_length=100)

class Personal(models.Model):
    user = models.OneToOneField(User, related_name='personal', on_delete=models.CASCADE)
    department = models.CharField(max_length=100)


TIPO_REFUGIO_CHOICES = [
    ('C', 'Campestre'),
    ('U', 'Urbano'),
]

class Refugio(models.Model):
    nombre = models.CharField(max_length=144, 
                              blank=False, 
                              null=False, 
                              verbose_name='Nombre del refugio',
                              help_text='El nombre comercial del refugio o el nombre corto')
    direccion = models.CharField(max_length=144, blank=True)
    tipo = models.CharField(max_length=5, blank=True, choices=TIPO_REFUGIO_CHOICES)
    descripcion = models.TextField(blank=True, null=True)
    ciudad = models.CharField(max_length=144, blank=False, null=False, default='Quito')
    fecha_actualizacion = models.DateTimeField(
        default=timezone.now, 
        verbose_name='fecha de actualización',
        help_text='Fecha de la última actualización del registro.'
    )
    es_activo = models.BooleanField(blank=False, 
                                    null=False, 
                                    default=True, 
                                    verbose_name='¿Propiedad activa?')
    
    documento = models.FileField(
        upload_to="documentos/", 
        blank=True, 
        verbose_name='documentos del refugio',
        help_text='Documento del refugio'
    )

    def __str__(self) -> str:
        return f'{self.pk} - {self.nombre}'
    
    def get_absolute_url(self):
        return reverse('ver_refugio', kwargs={'codigo_refugio': self.id})
    
    def get_edit_url(self):
        return reverse('editar_refugio', kwargs={'codigo_refugio': self.id})
    
    def get_delete_url(self):
        return reverse('eliminar_refugio', kwargs={'codigo_refugio': self.id})
    
    def cantidad_perros(self):
        return self.perros.count()


SEXO_CHOICES = [
    ('M', 'Macho'),
    ('F', 'Hembra'),
]

ESTERILIZADO_CHOICES = [
    (True, 'Sí'),
    (False, 'No'),
]

class Perro(models.Model):
    nombre = models.CharField(
        max_length=144, 
        blank=False, 
        null=False, 
        verbose_name='nombre',
        help_text='Nombre completo del perro.'
    )
    descripcion = models.TextField(
        blank=True, 
        null=True, 
        verbose_name='descripción',
        help_text='Descripción detallada del perro.'
    )
    sexo = models.CharField(
        max_length=1, 
        blank=False, 
        null=False, 
        choices=SEXO_CHOICES, 
        verbose_name='sexo',
        help_text='Sexo del perro.'
    )
    esterilizado = models.BooleanField(
        default=False, 
        choices=ESTERILIZADO_CHOICES, 
        verbose_name='esterilizado',
        help_text='Indica si el perro está esterilizado.'
    )
    ficha_perro = models.FileField(
        upload_to="uploads/", 
        blank=True, 
        verbose_name='ficha del perro',
        help_text='Ficha médica del perro.'
    )
    fecha_nacimiento = models.DateField(
        blank=True, 
        null=True, 
        verbose_name='fecha de nacimiento',
        help_text='Fecha de nacimiento del perro.'
    )
    fecha_actualizacion = models.DateTimeField(
        default=timezone.now, 
        verbose_name='fecha de actualización',
        help_text='Fecha de la última actualización del registro.'
    )
    refugio_actual = models.ForeignKey(
        'Refugio', 
        related_name='perros', 
        on_delete=models.SET_NULL, 
        null=True, 
        verbose_name='refugio actual',
        help_text='Refugio en el que se encuentra actualmente el perro.'
    )
    foto = models.ImageField(
        upload_to="media/", 
        blank=True, 
        null=True, 
        verbose_name='foto',
        help_text='Foto del perro.',

    )

    class Meta:
        verbose_name = 'perro'
        verbose_name_plural = 'perros'
        ordering = ['nombre']

    def __str__(self):
        return self.nombre

    def calcular_edad(self):
        """Calcula la edad del perro a partir de su fecha de nacimiento."""
        if self.fecha_nacimiento:
            hoy = date.today()
            return hoy.year - self.fecha_nacimiento.year - ((hoy.month, hoy.day) < (self.fecha_nacimiento.month, self.fecha_nacimiento.day))
        else:
            return 'Desconocida'  # Devuelve un string en lugar de None para una mejor representación

    @property
    def edad(self):
        """Propiedad para obtener la edad calculada del perro."""
        return self.calcular_edad()
    
    

class AtencionesClinica(models.Model):
    perro = models.ForeignKey(Perro, on_delete=models.CASCADE)
    fecha_atencion = models.DateField()
    peso = models.FloatField()
    talla = models.FloatField()
    resumen = models.TextField()
    veterinario = models.CharField(max_length=100)

    def __str__(self):
        return f"Atención {self.fecha_atencion} para {self.perro.nombre}"

VACUNAS_CHOICES = [
    ('DHPP', 'Distemper, Hepatitis, Parainfluenza and Parvovirus'),
    ('RABIES', 'Rabies'),
    ('LEPTO', 'Leptospirosis'),
    ('BORDETELLA', 'Bordetella Bronchiseptica'),
    ('LYME', 'Lyme Disease'),
    ('GIARDIA', 'Giardia'),
    ('CORONA', 'Coronavirus'),
    ('HEARTWORM', 'Heartworm Prevention'),
    ('INFLUENZA', 'Canine Influenza'),
    ('PARVO', 'Parvovirus'),
    ('ADENO', 'Adenovirus'),
    ('DISTEMPER', 'Canine Distemper'),
    ('HEPATITIS', 'Infectious Canine Hepatitis'),
]

class Vacuna(models.Model):
    fecha_vacunacion = models.DateField()
    vacuna = models.CharField(max_length=100, choices=VACUNAS_CHOICES)
    certificado = models.CharField(max_length=100)
    perro = models.ForeignKey(Perro, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.vacuna} para {self.perro.nombre}"

class Persona(models.Model):
    nombre = models.CharField(max_length=100)
    ciudad = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)
    correo = models.EmailField()
    intereses = models.TextField()
    rol = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre


class InteresadosEnRescatar(models.Model):
    perro = models.ForeignKey(Perro, on_delete=models.CASCADE)
    persona = models.ForeignKey(Persona, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.persona.nombre} interesado en {self.perro.nombre}"



######
# SUPERSTORE
    
class Country(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class City(models.Model):
    name = models.CharField(max_length=100)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    state = models.CharField(max_length=100)
    postal_code = models.IntegerField()

    class Meta:
        unique_together = ('name', 'country', 'state', 'postal_code')

    def __str__(self):
        return f"{self.name}, {self.state}, {self.country.name}"

class Category(models.Model):
    name = models.CharField(max_length=100)
    sub_category = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} - {self.sub_category}"

class Product(models.Model):
    product_id = models.CharField(max_length=20)
    name = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
class Order(models.Model):
    order_id = models.CharField(max_length=20)
    order_date = models.DateField()
    ship_date = models.DateField()
    ship_mode = models.CharField(max_length=50)
    customer_id = models.CharField(max_length=20)
    customer_name = models.CharField(max_length=100)
    segment = models.CharField(max_length=50)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    region = models.CharField(max_length=50)

    def __str__(self):
        return self.order_id
    
class OrderLine(models.Model):
    order = models.ForeignKey(Order, related_name='order_lines', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    sales = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()
    discount = models.DecimalField(max_digits=5, decimal_places=2)
    profit = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.order.order_id} - {self.product.name}"