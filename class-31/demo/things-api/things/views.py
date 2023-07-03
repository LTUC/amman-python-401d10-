from django.shortcuts import render
from rest_framework import generics
from .models import Thing 
from .serializers import ThingSerializer

# Create your views here.

# ListAPIView
class ThingsList(generics.ListCreateAPIView):
    queryset = Thing.objects.all()
    serializer_class = ThingSerializer

# RetrieveAPIView RetrieveUpdateAPIView
class ThingDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Thing.objects.all()
    serializer_class = ThingSerializer
