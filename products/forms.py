from django import forms
from django.forms import ModelForm
from .models import Product

# create form based on the Product model
class ProductForm(ModelForm):
    class Meta: 
        model = Product
        # Define the inputs to display
        fields = ('name', 'price', 'price_id')
