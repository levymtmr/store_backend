from django.db import models
from products.models import Product


class OrderDetail(models.Model):
    products = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    quantity = models.IntegerField()
    discount = models.DecimalField(max_digits=5, decimal_places=3)
    total = models.DecimalField(max_digits=6, decimal_places=2)
