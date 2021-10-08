from django import forms
from .models import offering


class OfferingForm(forms.ModelForm):
    class Meta:
        model = offering
        fields = ('work_category', 'work_details', 'offering_image') 

        widgets = {
            'work_category': forms.TextInput(attrs={'class': 'input3', 'type': "text", 'name': "work_category", 'placeholder': "Fruit Picking"}),
            'work_details': forms.Textarea(attrs={'class': 'input3', 'type': "text", 'name': "work_details", 'placeholder': "Short description of the work involved"}),
        }