from rest_framework import viewsets
from sells.models import Sell
from sells.serializers import SellSerializer, SellListSerializer
from rest_framework.response import Response


class SellViewSet(viewsets.ModelViewSet):
    queryset = Sell.objects.all()
    serializer_class = SellSerializer

    def list(self, request):
        serializer = SellListSerializer(self.queryset, many=True)
        return Response(serializer.data)