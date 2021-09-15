from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django_countries.fields import CountryField
from django.contrib.auth.models import User

# Create your models here.
class offering(models.Model):
    name = models.CharField(max_length=20)
    nationality = CountryField()
    first_language = models.CharField(max_length=20)
    location = models.CharField(max_length=20)
    work_category = models.CharField(max_length=20)
    work_details = models.TextField()
    email = models.EmailField(max_length=20)
    phonenumber = PhoneNumberField()
    host = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.name