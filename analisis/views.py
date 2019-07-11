from rest_framework import generics
from sells.models import Sell
from rest_framework.views import APIView
from rest_framework.response import Response

class AnalisisView(APIView):

    def get(self, request, format=None):
        serializer = {}
        return Response(serializer.data)




