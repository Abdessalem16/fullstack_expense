from django.shortcuts import render
from rest_framework import generics

from api.models import Transaction
from api.serializers import TransactionSerializer

class TransactionListCreateView(generics.ListCreateAPIView):
    queryset =Transaction.objects.all()
    serializer_class = TransactionSerializer
    

