from rest_framework import serializers
from products.models import Product, Storage, Sell, Client, Cart


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ("__all__")


class StorageSerializer(serializers.ModelSerializer):
    product = serializers.SlugRelatedField(queryset=Product.objects.all(), slug_field='name')

    class Meta:
        model = Storage
        fields = ("id", "product", "amount", "total", "date_storage")


class SellSerializer(serializers.ModelSerializer):
    # products = serializers.ManyRelatedField(child_relation="products")
    # products = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all(), many=True)

    class Meta:
        model = Sell
        fields = ("amount", "products")


class ClientSerializer(serializers.ModelSerializer):

    class Meta:
        model = Client
        fields = ("__all__")


class CartSerializer(serializers.ModelSerializer):
    client = serializers.SlugRelatedField(queryset=Client.objects.all(), slug_field='name')

    class Meta:
        model = Cart
        fields = ("client", "sell_itens")