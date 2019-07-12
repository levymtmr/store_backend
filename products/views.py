from django_filters.rest_framework import DjangoFilterBackend
from idna import unicode
from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.filters import SearchFilter
from rest_framework import permissions
from rest_framework.response import Response

from products.models import Product
from products.serializers import ProductSerializer


class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    filter_backends = (DjangoFilterBackend, SearchFilter)
    search_fields = ('^name', '^date')










