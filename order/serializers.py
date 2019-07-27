from rest_framework import serializers
from order.models import Order
from order_details.models import OrderDetail


class OrderDetailSerializer(serializers.Serializer):
    products = serializers.CharField(required=False)
    price = serializers.CharField(required=False)
    quantity = serializers.IntegerField()
    discount = serializers.DecimalField(max_digits=5, decimal_places=3)
    total = serializers.DecimalField(max_digits=6, decimal_places=2)
    user = serializers.CharField(required=False)


class OrderSerializer(serializers.ModelSerializer):
    order_details = OrderDetailSerializer(many=True)
    class Meta:
        model = Order
        fields = ("order_date", "ship_date", "payment", "active", "user", "order_details")
