from django.db import models


class Product(models.Model):
    UNIT_CHOICES = (
        ('Kg', 'kg'),
        ('UND', 'und'),
        ('SC', 'sc')
    )

    name = models.CharField(max_length=200)
    date = models.DateField()
    unit = models.CharField(max_length=3, choices=UNIT_CHOICES, default='UND')
    price = models.DecimalField(max_digits=7, decimal_places=3)
    amount = models.DecimalField(max_digits=6, decimal_places=2)
    
    def __str__(self):
        return self.name

    class Meta:
        unique_together = ('name',)

    def save(self, *args, **kwargs):
        return super().save(*args, **kwargs)



    # def empty_cart(self, items):
    #     validate = False
    #     if items.count != 0:
    #         validate = True
    #     return validate


    # @property
    # def total(self):
    #     sum = 0
    #     for item in self.buy_itens:
    #         sum += item.products.price
    #     return sum


    # def save(self, *args, **kwargs):
    #     if self.empty_cart(self.buy_itens):
    #         return super().save(*args, **kwargs)





