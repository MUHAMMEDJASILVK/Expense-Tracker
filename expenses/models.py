from django.db import models
from django.contrib.auth.models import User


class Income(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    source = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
   
    def __str__(self):
        return self.source

class Expense(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    Expensename = models.CharField(max_length=100)
    category = models.CharField(max_length=100, default='Other')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    description = models.TextField(blank=True)

    def __str__(self):
        return self.Expensename