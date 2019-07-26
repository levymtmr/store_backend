from rest_framework import viewsets
from order_details.models import OrderDetail
from order_details.serializers import OrderDetailSerializer


class OrderDetailViewSet(viewsets.ModelViewSet):
    queryset = OrderDetail.objects.all()
    serializer_class = OrderDetailSerializer
