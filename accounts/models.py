from django.db import models
from django.contrib.auth.models import User

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


class Payment(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=1)
    account_choices = [
        ('paid', 'paid'),
        ('unpaid', 'unpaid')]
    payment_status = models.CharField(
        max_length=6,
        choices=account_choices)
    def __str__(self):
        return self.payment_status

        
        




