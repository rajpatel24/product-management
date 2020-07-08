from django.db import models

# Create your models here.


CATEGORIES = (
    ('phone', 'Mobiles'),
    ('tv', 'SmartTV'),
    ('computer', 'Laptop'),
    ('earphone', 'Handsfree'),

)

QUANTITY = (
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5'),
)

class Product(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=10, choices=CATEGORIES)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    quantity = models.CharField(max_length=10, choices=QUANTITY)
    short_description = models.CharField(max_length=50)
    long_description = models.CharField(max_length=100)

