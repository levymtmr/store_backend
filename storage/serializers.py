from rest_framework import serializers
from storage.models import Storage
from products.models import Product


class StorageSerializer(serializers.ModelSerializer):
    product = serializers.SlugRelatedField(queryset=Product.objects.all(), slug_field='name')

    class Meta:
        model = Storage
        fields = ("id", "product", "amount", "total", "date_storage", "price")
