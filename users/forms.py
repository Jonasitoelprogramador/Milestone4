from django import forms
from .models import Host


class HostForm(forms.ModelForm):
    class Meta:
        model = Host
        fields = ('nationality', 'first_language', 'location') 
         
        widgets = {
            'nationality': forms.TextInput(attrs={'class': 'input3', 'type': "text", 'name': "nationality", 'placeholder': "French"}),
            'first_language': forms.Textarea(attrs={'class': 'input3', 'type': "text", 'name': "first_language", 'placeholder': "Chinese"}),
            'location': forms.TextInput(attrs={'class': 'input3', 'type': "text", 'name': "location", 'placeholder': "Mauritiaus"}),
        }
