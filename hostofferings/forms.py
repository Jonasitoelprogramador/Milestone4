from django import forms
from .models import offering


class OfferingForm(forms.ModelForm):
    class Meta:
        model = offering
        fields = ('name', 'nationality', 'first_language', 'location', 'work_category', 'work_details', 'email') 

