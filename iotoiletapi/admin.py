from django.contrib import admin

# Register your models here.
from .models import SensorData


@admin.register(SensorData)
class SensorDataAdmin(admin.ModelAdmin):
    pass