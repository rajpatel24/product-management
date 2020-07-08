from django import forms
from .models import Product

class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = ('name', 'category', 'price', 'quantity', 'short_description', 'long_description')

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)
