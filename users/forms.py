from django import forms
from .models import Host, Worker
from django.forms import ModelForm


class HostCreationForm(ModelForm):
    class Meta:
        model = Host
        fields = ('nationality', 'first_language', 'location')

        widgets = {
            'nationality': forms.TextInput(attrs={'id':"nationality_first", 'placeholder': "Fruit Picking", 'class': 'input3'}),
            'first_language': forms.TextInput(attrs={'id':"first_language_desired", 'placeholder': "Fruit Picking", 'class': 'input3'}),
            'location': forms.TextInput(attrs={'id':"location_experience", 'placeholder': "Fruit Picking", 'class': 'input3'}),
        }


class WorkerCreationForm(ModelForm):
    class Meta:
        model = Worker
        fields = ('first_language', 'desired_language', 'nationality', 'work_experience_category', 'work_experience', 'worker_image')

        widgets = {
            'first_language': forms.TextInput(attrs={'id':"nationality_first", 'placeholder': "Fruit Picking", 'class': 'input3'}),
            'desired_language': forms.TextInput(attrs={'id':"first_language_desired", 'placeholder': "Fruit Picking", 'class': 'input3'}),
            'nationality': forms.TextInput(attrs={'id':"nationality", 'placeholder': "Austrian", 'class': 'input3'}),
            'work_experience_category': forms.TextInput(attrs={'id':"location_experience", 'placeholder': "Fruit Picking", 'class': 'input3'}),
            'work_experience': forms.TextInput(attrs={'id': "work_experience", 'placeholder': "I worked on a farm for 3 months...", 'class': 'input3'}),
        }


