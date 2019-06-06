from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.filters import SearchFilter

from bills.models import Bill
from bills.serializers import BillSerializer


class BillViewSet(viewsets.ModelViewSet):
    queryset = Bill.objects.all()
    serializer_class = BillSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter)
    search_fields = ('^category', '^payday', '^description')

