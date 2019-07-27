from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework import generics
from rest_framework import permissions


from users.serializers import UserSystemSerializer


class UserSystem(viewsets.ModelViewSet):
    pass


class CreateUserView(generics.CreateAPIView):
    model = get_user_model()
    permission_classes = (permissions.AllowAny,)
    serializer_class = UserSystemSerializer

