

from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from users.models import Host, Worker


class ExtendedUserCreationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ("username", "email", "first_name", "last_name", "password1", "password2")

    widgets = {
            'username': forms.TextInput(attrs={'id':"username1", 'class': 'background-translucent'}),
            'email': forms.TextInput(attrs={'id':"first_language_desired", 'placeholder': "Fruit Picking", 'class': 'background-translucent'}),
            'first_name': forms.TextInput(attrs={'id':"location_experience", 'placeholder': "Fruit Picking", 'class': 'background-translucent'}),
            'last_name': forms.TextInput(attrs={'id': "work_experience", 'placeholder': "I worked on a farm for 3 months...", 'class': 'background-translucent'}),
            'password1': forms.TextInput(attrs={'id': "work_experience", 'placeholder': "I worked on a farm for 3 months...", 'class': 'background-translucent'}),
            'password2': forms.TextInput(attrs={'id': "work_experience", 'placeholder': "I worked on a farm for 3 months...", 'class': 'background-translucent'}),
        }


    def save(self, commit=True):
        user = super().save(commit=True)

        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']

        if commit:
            user.save()
        return user


class HostCreationForm(ModelForm):
    class Meta:
        model = Host
        fields = ('nationality', 'first_language', 'location')

        widgets = {
            'nationality': forms.TextInput(attrs={'id':"nationality_first", 'placeholder': "Fruit Picking", 'class': 'background-translucent'}),
            'first_language': forms.TextInput(attrs={'id':"first_language_desired", 'placeholder': "Fruit Picking", 'class': 'background-translucent'}),
            'location': forms.TextInput(attrs={'id':"location_experience", 'placeholder': "Fruit Picking", 'class': 'background-translucent'}),
        }


class WorkerCreationForm(ModelForm):
    class Meta:
        model = Worker
        fields = ('first_language', 'desired_language', 'work_experience_category', 'work_experience')

        widgets = {
            'first_language': forms.TextInput(attrs={'id':"nationality_first", 'placeholder': "Fruit Picking", 'class': 'background-translucent'}),
            'desired_language': forms.TextInput(attrs={'id':"first_language_desired", 'placeholder': "Fruit Picking", 'class': 'background-translucent'}),
            'work_experience_category': forms.TextInput(attrs={'id':"location_experience", 'placeholder': "Fruit Picking", 'class': 'background-translucent'}),
            'work_experience': forms.TextInput(attrs={'id': "work_experience", 'placeholder': "I worked on a farm for 3 months...", 'class': 'background-translucent'}),
        }


#class UserLoginForm(forms.Form):
#    username_or_email = forms.CharField()
#    password = forms.CharField(widget=forms.PasswordInput)