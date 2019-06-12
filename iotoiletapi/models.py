from django.db import models
from iotoiletapp.models import SensorData as sd
# Create your models here.

class SensorData(models.Model):
    timestamp = sd.timestamp
    sensor_id = sd.sensor_id
    value1 = sd.value1