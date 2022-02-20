from django.db import models
from django.contrib.auth.models import User

class Type(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=1)
    account_choices = [
        ('host', 'host'),
        ('worker', 'worker')]
    account_type = models.CharField(
        max_length=6,
        choices=account_choices)

    def __str__(self):
        return self.account_type


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

        
        




