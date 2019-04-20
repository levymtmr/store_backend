from rest_framework import viewsets
from cart.models import Cart
from cart.serializers import CartSerializer, CartListModelSerializer
from rest_framework.response import Response
from sells.models import Sell

from rest_framework import mixins


class CartViewSet(viewsets.ModelViewSet, mixins.CreateModelMixin):
    queryset = Cart.objects.all()
    serializer_class = CartListModelSerializer

    def list(self, request):
        serializer = CartSerializer(self.queryset, many=True)
        return Response(serializer.data)

    # def create(self, request):
    #     seralizer = CartListModelSerializer(Sell.objects.all(), many=True)
    #     print(seralizer.data)
    #     return Response(seralizer.data)





