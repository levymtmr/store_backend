from django.db import models
from products.models import Product


class Storage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=6, decimal_places=2)
    date_storage = models.DateField()

    def __str__(self):
        return self.product.name

    @property
    def price(self):
        return self.product.price

    @property
    def total(self):
        return self.product.price * self.amount