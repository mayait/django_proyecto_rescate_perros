# Generated by Django 4.2.10 on 2024-02-20 00:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rescate_perros', '0013_category_city_country_order_product_orderline_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
