from django import forms
from .models import Offering

#based on Offering model 
class OfferingForm(forms.ModelForm):
    class Meta:
        model = Offering
        # define inputs to be displayed
        fields = ('work_category', 'work_details', 'offering_image') 

        # specify styling of inputs
        widgets = {
            'work_category': forms.TextInput(attrs={'class': 'input3', 'type': "text", 'name': "work_category", 'placeholder': "Fruit Picking"}),
            'work_details': forms.Textarea(attrs={'class': 'input3', 'type': "text", 'name': "work_details", 'placeholder': "Short description of the work involved", 'rows':"3"}),
        }


