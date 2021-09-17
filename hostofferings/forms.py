from django import forms
from .models import offering


class OfferingForm(forms.ModelForm):
    class Meta:
        model = offering
        fields = ('work_category', 'work_details') 

