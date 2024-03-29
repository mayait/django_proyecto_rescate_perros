import pandas as pd
from django.utils.dateparse import parse_date
from .models import Order, OrderLine, Product, Category, City, Country



import pandas as pd


def import_excel_to_django():
    # Cargar los datos desde Excel
    df = pd.read_excel('https://raw.githubusercontent.com/mayait/ClaseAnalisisDatos/main/machine_learning/datasets/superstore.xlsx')
    
    for _, row in df.iterrows():
        country_obj, _ = Country.objects.update_or_create(name=row['Country'])
        
        city_obj, _ = City.objects.update_or_create(
            name=row['City'],
            state=row['State'],
            postal_code=row['Postal Code'],
            country=country_obj
        )
        
        category_obj, _ = Category.objects.update_or_create(
            name=row['Category'],
            sub_category=row['Sub-Category']
        )
        
        product_obj, _ = Product.objects.update_or_create(
            product_id=row['Product ID'],
            name=row['Product Name'],
            category=category_obj
        )
        # print('Producto', product_obj, 'creado', _)
        
        order_obj, _ = Order.objects.update_or_create(
            order_id=row['Order ID'],
            defaults={
                'order_date': parse_date(row['Order Date'].strftime('%Y-%m-%d')),
                'ship_date': parse_date(row['Ship Date'].strftime('%Y-%m-%d')),
                'ship_mode': row['Ship Mode'],
                'customer_id': row['Customer ID'],
                'customer_name': row['Customer Name'],
                'segment': row['Segment'],
                'city': city_obj,
                'region': row['Region']
            }
        )
        
        OrderLine.objects.create(
            order=order_obj,
            product=product_obj,
            sales=row['Sales'],
            quantity=row['Quantity'],
            discount=row['Discount'],
            profit=row['Profit']
        )


def contar_frecuencia_palabras(texto):
    a = 1
    return None



def traducir(text, dest='en', **kwargs):
    a = 1
    return text
    