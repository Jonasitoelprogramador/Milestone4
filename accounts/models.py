from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Host(User):
    nationality = models.CharField(max_length=100)
    first_language = models.CharField(max_length=100)
    location = models.CharField(max_length=100)


class Worker(User):
    nationality = models.CharField(max_length=100)
    first_language = models.CharField(max_length=100)
    desired_language = models.CharField(max_length=100)
    work_experience_category = models.CharField(max_length=100)
    work_experience = models.CharField(max_length=100)
    


        
        




