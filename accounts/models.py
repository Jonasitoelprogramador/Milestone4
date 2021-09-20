from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Host(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nationality = models.CharField(max_length=100, default='British')
    first_language = models.CharField(max_length=100, default='British')
    location = models.CharField(max_length=100, default='Britain')

    def __init__(self, username):
        self.username = username

    def __str__(self):
        return self.username


class Worker(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nationality = models.CharField(max_length=100)
    first_language = models.CharField(max_length=100)
    desired_language = models.CharField(max_length=100)
    work_experience_category = models.CharField(max_length=100)
    work_experience = models.CharField(max_length=100)

    def __str__(self):
        return self.username
    


        
        




