from django import forms
from .models import Host, Worker


class UserLoginForm(forms.Form):
    username_or_email = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class HostCreationForm(forms.ModelForm):
    class Meta:
        model = Host
        fields = ('nationality', 'first_language', 'location', 'email', 'username', 'password') 


class WorkerCreationForm(forms.ModelForm):
    class Meta:
        model = Worker
        fields = ('email', 'username', 'password', 'nationality', 'first_language', 'desired_language', 'work_experience_category', 'work_experience') 
