# from django import forms
# from .models import Host, Worker


# class UserLoginForm(forms.Form):
#     username_or_email = forms.CharField()
#     password = forms.CharField(widget=forms.PasswordInput)


# class HostCreationForm(forms.ModelForm):
#     class Meta:
#         model = Host
#         fields = ('nationality', 'first_language', 'location', 'email', 'username', 'password') 


# class WorkerCreationForm(forms.ModelForm):
#     class Meta:
#         model = Worker
#         fields = ('email', 'username', 'password', 'nationality', 'first_language', 'desired_language', 'work_experience_category', 'work_experience') 

from django.forms import forms, ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from users.models import Host, Worker


class ExtendedUserCreationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ("username", "email", "first_name", "last_name", "password1", "password2")

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


class WorkerCreationForm(ModelForm):
    class Meta:
        model = Worker
        fields = ('first_language', 'desired_language', 'work_experience_category', 'work_experience')


#class UserLoginForm(forms.Form):
#    username_or_email = forms.CharField()
#    password = forms.CharField(widget=forms.PasswordInput)