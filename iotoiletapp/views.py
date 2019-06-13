import psycopg2
from django.shortcuts import render

from iotoiletapp.forms import IotoiletappForm

CONN = "host=ytakashina.cp12crxu8zls.ap-northeast-1.rds.amazonaws.com" + \
       " port=5432 dbname=postgres user=postgres password=postgres"

SQL_AVAILABLE_TOILETS = """
select
    floor_name,
    count(room_type_name='男性用' or null) as male_empty,
    count(room_type_name='女性用' or null) as female_empty
from (
    select
        *
    from
        iotoiletapp_sensordata as SD
        left outer join iotoiletapp_sensor as S on S.id = SD.sensor_id_id
        left outer join iotoiletapp_toilet as T on S.toilet_id_id = T.id
        left outer join iotoiletapp_room as R on T.room_id_id = R.id
        left outer join iotoiletapp_roomtype as RT on R.room_type_id_id = RT.id
        left outer join iotoiletapp_floor as F on F.id = R.floor_id_id
        where (sensor_id_id, timestamp)
        in (select sensor_id_id, max(timestamp) from iotoiletapp_sensordata group by sensor_id_id)
) as sub
group by floor_name;
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
