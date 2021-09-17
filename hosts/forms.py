from django import forms
from .models import Host


class HostForm(forms.ModelForm):
    class Meta:
        model = Host
        fields = ('name', 'nationality', 'first_language', 'location', 'email') 
