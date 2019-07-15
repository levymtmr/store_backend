from requests import Response
from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated

from client.models import Client
from client.serializers import ClientSerializer


class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    # authentication_classes = (SessionAuthentication, BasicAuthentication)
    # permission_classes = (IsAuthenticated,)

    # def get(self, request, format=None):
    #     content = {
    #         'user': request.user,  # `django.contrib.auth.User` instance.
    #         'auth': request.auth,  # None
    #     }
    #     return Response(content)