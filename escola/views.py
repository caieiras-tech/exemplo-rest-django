from django.shortcuts import render
from rest_framework import viewsets
from escola.models import Escola
from escola.serializers import EscolaSerializer

# Create your views here.

class EscolaViewSet(viewsets.ModelViewSet):
    queryset = Escola.objects.all()
    serializer_class = EscolaSerializer
