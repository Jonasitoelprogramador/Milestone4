from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from users.models import Host, Worker
from .models import Role

# This is a standard Django user creation form with password1 and password 2 fields added
class ExtendedUserCreationForm(UserCreationForm):
    # extra field
    password1 = forms.CharField(
            label="Password",
            widget=forms.PasswordInput(attrs={'class':'login-inputs', 'type':'password'}),
        )
    # extra field
    password2 = forms.CharField(
        label="Confirm password",
        widget=forms.PasswordInput(attrs={'class':'login-inputs', 'type':'password'}),
    )

    class Meta:
        model = User
        # define which model fields should have a form input
        fields = ("username", "email", "first_name", "last_name", "password1", "password2")

        # used to style the form inputs using login-inputs css class
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

# based on Role model
class RoleForm(ModelForm):
    class Meta:
        model = Role
        # defines the inouts to display
        fields = ("account_Role",)
        # used to add styling via host_vs_worker css class
        widgets = {
            "account_Role": forms.Select(attrs={'class': 'host_vs_worker'})
        }


class UserEmailForm(ModelForm):
    class Meta:
        model = User
        fields = ("email",)

        widgets = {
            'email': forms.TextInput(attrs={'id':"email", 'class': 'input3'})
        }