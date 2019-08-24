from rest_framework import viewsets
from order.models import Order
from order.serializers import OrderSerializer
from order.serializers import GetOrderSerializer
from rest_framework.response import Response


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def list(self, request, *args, **kwargs):
        serializer = GetOrderSerializer(data=self.queryset, many=True)
        serializer.is_valid(raise_exception=False)
        return Response(data=serializer.data)

