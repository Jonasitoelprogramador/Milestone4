from django.db import models

#Create your models here.
class Host(models.Model):
    name = models.CharField(max_length=100)
    nationality = CountryField()
    first_language = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)

    def __str__(self):
        return self.name