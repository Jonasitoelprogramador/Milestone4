from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from users.models import Host, Worker
from .models import Type

class ExtendedUserCreationForm(UserCreationForm):
    password1 = forms.CharField(
            label="Password",
            widget=forms.PasswordInput(attrs={'class':'login-inputs', 'type':'password'}),
        )
    password2 = forms.CharField(
        label="Confirm password",
        widget=forms.PasswordInput(attrs={'class':'login-inputs', 'type':'password'}),
    )

    class Meta:
        model = User
        fields = ("username", "email", "first_name", "last_name", "password1", "password2")

        widgets = {
                'username': forms.TextInput(attrs={'id':"username", 'class': 'login-inputs'}),
                'email': forms.TextInput(attrs={'id':"email", 'class': 'login-inputs'}),
                'first_name': forms.TextInput(attrs={'id':"first_name", 'class': 'login-inputs'}),
                'last_name': forms.TextInput(attrs={'id': "last_name", 'class': 'login-inputs'}),
            }

    def save(self, commit=True):
        user = super().save(commit=True)

        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']

        if commit:
            user.save()
        return user


class UserEmailForm(ModelForm):
    class Meta:
        model = User
        fields = ("email",)

        widgets = {
            'email': forms.TextInput(attrs={'id':"email", 'class': 'input3'})
        }


class TypeForm(ModelForm):
    class Meta:
        model = Type
        fields = ("account_type",)

        widgets = {
            "account_type": forms.Select(attrs={'class': 'host_vs_worker'})
        }