from django.db import models
from payment.models import Payment
from order_details.models import OrderDetail
from django.contrib.auth.models import User


class Order(models.Model):
    order_date = models.DateField(auto_now=True)
    ship_date = models.DateField(auto_now=True)
    payment = models.ForeignKey(Payment, on_delete=models.CASCADE)
    # active = models.BooleanField()
    order_details = models.ManyToManyField(OrderDetail)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
