from django_filters.rest_framework import DjangoFilterBackend, OrderingFilter
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.filters import SearchFilter

from sells.models import Sell
from sells.serializers import SellSerializer, SellListSerializer
from rest_framework.response import Response
from rest_framework import mixins



class SellViewSet(viewsets.ModelViewSet, mixins.CreateModelMixin):
    queryset = Sell.objects.all()
    serializer_class = SellSerializer
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)

    # def create(self, request, *args, **kwargs):
    #     serializer = SellSerializer(request.data)
    #     return Response(serializer.data)

    def list(self, request):
        serializer = SellListSerializer(Sell.objects.all().order_by("date").reverse(), many=True)
        return Response(serializer.data)

    @action(methods=['get'], detail=True, url_path="buscar", url_name="buscar")
    def buscar(self, request):
        pass



