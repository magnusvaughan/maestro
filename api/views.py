from django.shortcuts import render

# Create your views here.
from .models import Resource
from .serializers import ResourceSerializer
from rest_framework import generics

class ResourceListCreate(generics.ListCreateAPIView):
    queryset = Resource.objects.all()
    serializer_class = ResourceSerializer