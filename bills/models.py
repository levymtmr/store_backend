from django.db import models

class Bill(models.Model):
    description = models.CharField(max_length=250)
    payday = models.DateField()
    price = models.DecimalField(max_digits=7, decimal_places=3)
    category = models.CharField(max_length=200)
