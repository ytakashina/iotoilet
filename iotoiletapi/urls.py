from rest_framework import routers
from .views import SensorDataViewSet


router = routers.DefaultRouter()
router.register(r'sensordatas', SensorDataViewSet)
