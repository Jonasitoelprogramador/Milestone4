from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django_countries.fields import CountryField
from django.contrib.auth.models import User

# Create your models here.
class offering(models.Model):
    #name = models.CharField(max_length=100)
    #nationality = CountryField()
    #first_language = models.CharField(max_length=100)
    #location = models.CharField(max_length=100)
    work_category = models.CharField(max_length=100)
    work_details = models.TextField()
    #email = models.EmailField(max_length=100)
    host = models.ForeignKey(User, on_delete=models.CASCADE, null=True)


    def __str__(self):
        return self.name