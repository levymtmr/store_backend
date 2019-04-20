from django.db import models
from client.models import Client
from sells.models import Sell


class Cart(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    sell_itens = models.ManyToManyField(Sell, related_name="sell_itens")

