from django import forms
from django.forms import ModelForm
from .models import Product

# create form based on the Product model
class ProductForm(ModelForm):
    class Meta: 
        model = Product
        # Define the inputs to display
        fields = ('name', 'price', 'price_id')

        widgets = {
            'name': forms.TextInput(attrs={'id':"product-name", 'class': 'admin-form'}),
            'price': forms.TextInput(attrs={'id':"product-price", 'class': 'admin-form'}),
            'price_id': forms.TextInput(attrs={'id':"product-price-id", 'class': 'admin-form'}),
        }
