from django.contrib import admin
from .models import ToiletStatusType, Map, Floor, User, SensorStatusType, \
    SensorType, Sensor, Sex, SexRoomType, RoomType, Room, Toilet

admin.site.register(ToiletStatusType)
admin.site.register(Map)
admin.site.register(Floor)
admin.site.register(User)
admin.site.register(SensorStatusType)
admin.site.register(SensorType)
admin.site.register(Sensor)
admin.site.register(Sex)
admin.site.register(SexRoomType)
admin.site.register(RoomType)
admin.site.register(Room)
admin.site.register(Toilet)
# Register your models here.
