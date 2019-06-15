from rest_framework import serializers
from sells.models import Sell


class SellListSerializer(serializers.Serializer):
    date = serializers.CharField(read_only=True)
    products = serializers.CharField(read_only=True)
    client = serializers.CharField(read_only=True)
    amount = serializers.DecimalField(max_digits=7, decimal_places=3,read_only=True)
    unit = serializers.CharField(read_only=True)
    price = serializers.IntegerField(read_only=True)
    products_storage = serializers.CharField(read_only=True)


class SellSerializer(serializers.ModelSerializer):

    class Meta:
        model = Sell
        fields = ("__all__")



