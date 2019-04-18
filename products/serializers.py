from rest_framework import serializers
from products.models import Product, Storage, Sell, Client, Cart


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ("__all__")

class ProductSearchSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ("__all__")

class StorageSerializer(serializers.ModelSerializer):
    product = serializers.SlugRelatedField(queryset=Product.objects.all(), slug_field='name')

    class Meta:
        model = Storage
        fields = ("id", "product", "amount", "total", "date_storage", "price")


class SellListSerializer(serializers.Serializer):
    date = serializers.CharField(read_only=True)
    products = serializers.CharField(read_only=True)
    client = serializers.CharField(read_only=True)
    amount = serializers.IntegerField(read_only=True)
    unit = serializers.CharField(read_only=True)
    price = serializers.IntegerField(read_only=True)


class SellSerializer(serializers.ModelSerializer):

    class Meta:
        model = Sell
        fields = ("__all__")


class ClientSerializer(serializers.ModelSerializer):

    class Meta:
        model = Client
        fields = ("__all__")


class CartSerializer(serializers.ModelSerializer):
    client = serializers.SlugRelatedField(queryset=Client.objects.all(), slug_field='name')

    class Meta:
        model = Cart
        fields = ("__all__")

class CartListSerializer(serializers.Serializer):
    client = serializers.CharField(read_only=True)
    sell_itens = SellListSerializer()


