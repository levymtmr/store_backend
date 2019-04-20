from django_filters import FilterSet, filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.filters import OrderingFilter, SearchFilter
from products.models import Product
from products.serializers import ProductSerializer


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









