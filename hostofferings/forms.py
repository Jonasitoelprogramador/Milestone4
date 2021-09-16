from django import forms
from .models import offering


class offeringForm(forms.ModelForm):
    class Meta:
        model = offering
        fields = ('name', 'nationality', 'first_language', 'location', 'work_category', 'work_details', 'email') 

