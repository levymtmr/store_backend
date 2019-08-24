from django.db import models
from products.models import Product
from django.contrib.auth.models import User


class OrderDetail(models.Model):
    products = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    quantity = models.IntegerField()
    discount = models.DecimalField(max_digits=5, decimal_places=3, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        codigo = str(self.pk)
        return codigo

    @property
    def total(self):
        return self.quantity * self.price
