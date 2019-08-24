from rest_framework import serializers
from order_details.models import OrderDetail


class OrderDetailSerializer(serializers.ModelSerializer):
    discount = serializers.DecimalField(max_digits=5, decimal_places=3, allow_null=True)
    class Meta:
        model = OrderDetail
        fields = ('id', 'price', 'quantity', 'discount', 'products', 'user', 'total')
