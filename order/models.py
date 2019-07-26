from django.db import models
from payment.models import Payment
from order_details.models import OrderDetail


class Order(models.Model):
    order_date = models.DateField()
    ship_date = models.DateField()
    payment = models.ForeignKey(Payment, on_delete=models.CASCADE)
    active = models.BooleanField()
    order_details = models.ManyToManyField(OrderDetail)
