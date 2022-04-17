from django.db import models
from django.contrib.auth.models import User

# Role model contains id field, user field (1-to-1), account_Role (two options: host/worker)
class Role(models.Model):
    id = models.AutoField(primary_key = True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    account_choices = [
        ('host', 'host'),
        ('worker', 'worker')]
    account_Role = models.CharField(
        max_length=6,
        choices=account_choices)

    def __str__(self):
        return self.account_Role



        
        




