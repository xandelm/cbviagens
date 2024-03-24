from django.shortcuts import render
from rest_framework import viewsets
from .serializers import TransportSerializer
from .models import Transport

class TransportViewSet(viewsets.ModelViewSet):
    queryset = Transport.objects.all()
    serializer_class = TransportSerializer

