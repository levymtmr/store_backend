from django.db import models
from products.models import Product
from client.models import Client
from storage.models import Storage


class Sell(models.Model):
        UNIT_CHOICES = (
            ('KG', 'kg'),
            ('UND', 'und'),
            ('SC', 'sc')
        )
        date = models.DateField(auto_now=True)
        client = models.ForeignKey(Client, on_delete=models.CASCADE)
        products_storage = models.ForeignKey(Storage, on_delete=models.CASCADE)
        amount = models.DecimalField(max_digits=6, decimal_places=2)
        unit = models.CharField(max_length=3, choices=UNIT_CHOICES, default='UND')
        price = models.DecimalField(max_digits=6, decimal_places=2)

        def update_amount(self):
            pk = self.products_storage.id
            item_amout = Storage.objects.get(id=pk).amount
            new_amount = item_amout - self.amount
            if item_amout > 0 and new_amount > 0:
                Storage.objects.filter(id=pk).update(amount=new_amount)

        def save(self, *args, **kwargs):
            self.update_amount()
            # print("kweadsdasd", args)
            # self.client = Client.objects.filter(name=self.client)[0].pk
            # self.products_storage = Product.objects.filter(name=self.products_storage)[0].pk
            return super().save(*args, **kwargs)

        def __str__(self):
            return self.client.name
