from django.shortcuts import render

# Create your views here.
import django_filters
from rest_framework import viewsets, filters

from iotoiletapp.models import SensorData
from .serializer import SensorDataSerializer


class SensorDataViewSet(viewsets.ModelViewSet):
    queryset = SensorData.objects.all()
    serializer_class = SensorDataSerializer
