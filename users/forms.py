from django import forms
from .models import Host, Worker
from django.forms import ModelForm

# form based on Host model
class HostCreationForm(ModelForm):
    class Meta:
        model = Host
        # Define the inputs to display
        fields = ('nationality', 'first_language', 'location')

        # Define the styling of the inputs via the input3 css class
        widgets = {
            'nationality': forms.TextInput(attrs={'id':"nationality_first", 'placeholder': "Fruit Picking", 'class': 'input3'}),
            'first_language': forms.TextInput(attrs={'id':"first_language_desired", 'placeholder': "Fruit Picking", 'class': 'input3'}),
            'location': forms.TextInput(attrs={'id':"location_experience", 'placeholder': "Fruit Picking", 'class': 'input3'}),
        }

# form based on Worker model
class WorkerCreationForm(ModelForm):
    class Meta:
        model = Worker
        # Define the inputs to display
        fields = ('first_language', 'desired_language', 'nationality', 'work_experience_category', 'work_experience', 'worker_image')

        # Define the styling of the inputs via the input3 css class
        widgets = {
            'first_language': forms.TextInput(attrs={'id':"nationality_first", 'placeholder': "Fruit Picking", 'class': 'input3'}),
            'desired_language': forms.TextInput(attrs={'id':"first_language_desired", 'placeholder': "Fruit Picking", 'class': 'input3'}),
            'nationality': forms.TextInput(attrs={'id':"nationality", 'placeholder': "Austrian", 'class': 'input3'}),
            'work_experience_category': forms.TextInput(attrs={'id':"location_experience", 'placeholder': "Fruit Picking", 'class': 'input3'}),
            'work_experience': forms.Textarea(attrs={'id': "work_experience", 'placeholder': "I worked on a farm for 3 months...", 'class': 'input3', 'rows':"3"}),
        }


