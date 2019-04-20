from rest_framework import viewsets
from storage.models import Storage
from storage.serializers import StorageSerializer


class StorageViewSet(viewsets.ModelViewSet):
    queryset = Storage.objects.all()
    serializer_class = StorageSerializer