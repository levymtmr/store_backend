from django_filters import FilterSet, filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.filters import OrderingFilter, SearchFilter
from products.models import Product, Storage, Sell, Client, Cart
from products.serializers import (ProductSerializer, StorageSerializer,
                                  SellSerializer, ClientSerializer, CartSerializer, SellListSerializer, CartListSerializer)
from rest_framework.response import Response


class ProductFilter(FilterSet):
    name = filters.CharFilter('name')

    class Meta:
        model = Product
        fields = ("__all__")


class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filter_class = ProductFilter
    filter_fields = ('name',)
    ordering_fields = ('name',)
    ordering = ('name')
    search_fields = ('name','name')


class StorageViewSet(viewsets.ModelViewSet):
    queryset = Storage.objects.all()
    serializer_class = StorageSerializer

class SellViewSet(viewsets.ModelViewSet):
    queryset = Sell.objects.all()
    serializer_class = SellSerializer

    def list(self, request):
        serializer = SellListSerializer(self.queryset, many=True)
        return Response(serializer.data)


class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

class CartViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

    # def list(self, request):
    #     serializer = CartListSerializer(self.queryset, many=True)
    #     return Response(serializer.data)