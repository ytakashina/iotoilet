from django.db import transaction, connection
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from iotoiletapp.models import Toilet, Room, ToiletStatus
from iotoiletapp.forms import IotoiletappForm
import datetime
import psycopg2


def index(request):
    cursor = connection.cursor()
    sql = 'select T.toilet_name, ' +\
        'RT.room_type_name, F.floor_name, TST.toilet_status_type_name, SD.timestamp, SD.value1 ' +\
        'from iotoiletapp_toilet as T inner join iotoiletapp_room as R ' +\
        'on T.room_id_id = R.id ' +\
        'inner join iotoiletapp_roomtype as RT ' +\
        'on R.room_type_id_id = RT.id ' +\
        'inner join iotoiletapp_floor as F ' +\
        'on R.floor_id_id = F.id ' +\
        'inner join iotoiletapp_toiletstatus as TS ' +\
        'on T.id = TS.toilet_id_id ' +\
        'inner join iotoiletapp_toiletstatustype as TST ' +\
        'on TS.toilet_status_type_id_id = TST.id ' +\
        'inner join iotoiletapp_sensor as S ' +\
        'on T.id = S.toilet_id_id ' +\
        'inner join iotoiletapp_sensordata as SD ' +\
        'on S.id = SD.sensor_id_id'
    cursor.execute(sql, {})
    toilet_list = cursor.fetchall()
    return render(request, 'iotoiletapp/index.html', {'toilet_list': toilet_list})


def search(request):
    form = IotoiletappForm(request.GET or None)
    return render(request, 'iotoiletapp/forms.html', {"form": form})

# def detail(request, id=None):
#     toilet = Iotoiletapp.objects.get(floor_no=floor_no)
#     return render(request, 'iotoiletapp/detail.html', {'toilet': toilet})
