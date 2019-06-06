from rest_framework import viewsets
from storage.models import Storage
from storage.serializers import StorageSerializer
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response



class StorageViewSet(viewsets.ModelViewSet):
    queryset = Storage.objects.all()
    serializer_class = StorageSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    search_fields = ["product__name"]