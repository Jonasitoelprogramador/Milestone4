from django import forms
from .models import Host


class HostForm(forms.ModelForm):
    class Meta:
        model = offering
        fields = ('nationality', 'first_language', 'location') 
