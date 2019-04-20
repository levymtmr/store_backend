from rest_framework import serializers
from client.models import Client
from cart.models import Cart
from sells.serializers import SellListSerializer

class ItemSerializer(serializers.Serializer):
    date = serializers.CharField(read_only=True)
    products = serializers.CharField(read_only=True)
    client = serializers.CharField(read_only=True)
    amount = serializers.IntegerField(read_only=True)
    unit = serializers.CharField(read_only=True)
    price = serializers.IntegerField(read_only=True)


class CartSerializer(serializers.ModelSerializer):
    client = serializers.SlugRelatedField(queryset=Client.objects.all(), slug_field='name')
    sell_itens = ItemSerializer()

    class Meta:
        model = Cart
        fields = ("client", "sell_itens")

class CartListModelSerializer(serializers.ModelSerializer):
    # client = serializers.CharField(read_only=True)
    # sell_itens = ItemSerializer()

    class Meta:
        model = Cart
        fields = ("__all__")