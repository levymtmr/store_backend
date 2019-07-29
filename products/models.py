from django.db import models
from category.models import Category


class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=7, decimal_places=3)
    date = models.DateField()
    description = models.CharField(max_length=250)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    # picture = models.ImageField()
    quantity = models.DecimalField(max_digits=6, decimal_places=2)
    
    def __str__(self):
        return self.name

    class Meta:
        unique_together = ('name',)

    def save(self, *args, **kwargs):
        return super().save(*args, **kwargs)







