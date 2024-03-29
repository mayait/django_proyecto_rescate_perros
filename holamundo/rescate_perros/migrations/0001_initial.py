# Generated by Django 4.2.10 on 2024-02-08 01:07

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Perro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=144)),
                ('descripcion', models.TextField(blank=True, null=True)),
                ('ficha_perro', models.FileField(blank=True, upload_to='uploads/')),
                ('fecha_nacimiento', models.DateTimeField(blank=True)),
                ('fecha_actualizacion', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
