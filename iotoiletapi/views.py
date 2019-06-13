# Create your views here.
from rest_framework import viewsets

from iotoiletapp.models import SensorData
from .serializer import SensorDataSerializer


class SensorDataViewSet(viewsets.ModelViewSet):
    queryset = SensorData.objects.all()
    serializer_class = SensorDataSerializer
