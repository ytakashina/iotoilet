import psycopg2
from django.shortcuts import render

from iotoiletapp.forms import IotoiletappForm

CONN = "host=ytakashina.cp12crxu8zls.ap-northeast-1.rds.amazonaws.com" + \
       " port=5432 dbname=postgres user=postgres password=postgres"

SQL_AVAILABLE_TOILETS = """
select 
    T.toilet_name,
    RT.room_type_name,
    F.floor_name,
    TST.toilet_status_type_name,
    SD.timestamp,
    SD.value1
from
    iotoiletapp_toilet as T
left outer join iotoiletapp_room as R
    on T.room_id_id = R.id
left outer join iotoiletapp_roomtype as RT
    on R.room_type_id_id = RT.id
left outer join iotoiletapp_floor as F
    on R.floor_id_id = F.id
left outer join iotoiletapp_toiletstatus as TS
    on T.id = TS.toilet_id_id
left outer join iotoiletapp_toiletstatustype as TST
    on TS.toilet_status_type_id_id = TST.id
left outer join iotoiletapp_sensor as S
    on T.id = S.toilet_id_id
left outer join iotoiletapp_sensordata as SD
    on S.id = SD.sensor_id_id
"""


def index(request):
    form = IotoiletappForm(request.GET or None)
    with psycopg2.connect(CONN) as conn, conn.cursor() as cur:
        cur.execute(SQL_AVAILABLE_TOILETS, {})
        available_toilets = cur.fetchall()
    available_toilets = available_toilets or [(i, i + 1, i + 2) for i in range(10)]
    return render(request, 'iotoiletapp/index.html', {'available_toilets': available_toilets, 'form': form})

# def detail(request, id=None):
#     toilet = Iotoiletapp.objects.get(floor_no=floor_no)
#     return render(request, 'iotoiletapp/detail.html', {'toilet': toilet})
