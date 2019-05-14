from rest_framework import viewsets
from sells.models import Sell
from sells.serializers import SellSerializer, SellListSerializer
from rest_framework.response import Response
from rest_framework import mixins


class SellViewSet(viewsets.ModelViewSet, mixins.CreateModelMixin):
    queryset = Sell.objects.all()
    serializer_class = SellSerializer

    # def create(self, request, *args, **kwargs):
    #     serializer = SellSerializer(request.data)
    #     return Response(serializer.data)

    def list(self, request):
        serializer = SellListSerializer(Sell.objects.all().order_by("date").reverse(), many=True)
        return Response(serializer.data)



