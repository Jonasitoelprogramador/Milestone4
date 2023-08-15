from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
import random
import string
import os.path


def path_time(instance, filename):
    #takes the instance and the filename of the uploaded image
    #splits the filename from the extension
    extension = os.path.splitext(filename)[1]
    #assigns a random value to the random_identifier field of the model instance
    instance.random_identifier = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(16))
    #adds the correct file extension to this field
    instance.random_identifier = instance.random_identifier + extension
    upload = 'images/'
    #uploads the newly-renamed image to the images folder on the server
    return os.path.join(upload, instance.random_identifier)


# Create your models here.
# Model with 5 attribues
class Host(models.Model):
    # user field has one-to-one relationship User model
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nationality = models.CharField(max_length=100)
    first_language = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    # define the options available in the payment_status attribute
    account_choices = [
        ('paid', 'paid'),
        ('nonpaid', 'nonpaid')]
    payment_status = models.CharField(
        max_length=10,
        choices=account_choices, default="nonpaid") 
    
    def __str__(self):
        return self.user.username
    

# Model with 9 attribues
class Worker(models.Model):
    # user field has one-to-one relationship User model
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nationality = models.CharField(max_length=100)
    first_language = models.CharField(max_length=100)
    desired_language = models.CharField(max_length=100)
    work_experience_category = models.CharField(max_length=100)
    work_experience = models.TextField()
    worker_image = models.ImageField(upload_to=path_time, default='default.jpg')
    random_identifier = models.CharField(max_length=100)
    # define the options available in the payment_status attribute
    account_choices = [
        ('paid', 'paid'),
        ('nonpaid', 'nonpaid')]
    payment_status = models.CharField(
        max_length=10,
        choices=account_choices, default="nonpaid") 

    def __str__(self):
        return self.user.username

