from django.shortcuts import render, get_object_or_404, redirect #追加
from django.http import HttpResponse
from iotoiletapp.models import Toilet, Room, ToiletStatus
from iotoiletapp.forms import IotoiletappForm
import datetime
import psycopg2

CONN = "host=ytakashina.cp12crxu8zls.ap-northeast-1.rds.amazonaws.com" +\
" port=5432 dbname=postgres user=postgres password=postgres"

#一覧
def index(request):
    with psycopg2.connect(CONN) as conn, conn.cursor() as cur:
        sql = 'select T.toilet_name, ' +\
        'RT.room_type_name, F.floor_name, TST.toilet_status_type_name, SD.timestamp, SD.value1 ' +\
        'from iotoiletapp_toilet as T inner join iotoiletapp_room as R ' +\
        'on T.room_id_id = R.id ' +\
        'inner join iotoiletapp_roomtype as RT '+\
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
        cur.execute(sql, {})
        toilet_list = cur.fetchall()
    return render(request, 'iotoiletapp/index.html', {'toilet_list': toilet_list})
    # render : 書き出し request : クライアントからのリクエスト
    # index.htmlに辞書でデータを渡す

def search(request):
    # search画面で、性別と今いる階層を入力させる
    toilet = Iotoiletapp()
    form = IotoiletappForm(instance=toilet)
    return render(request, 'iotoiletapp/index.html', {"form": form, "id": id})

# # 保存
# def save(request):
#     inquiry = Inquiry()
#     form = InquiryForm(request.POST, instance=inquiry)

#     if form.is_valid():
#         inquiry = form.save(commit=False)
#         inquiry.save()
#     else:
#         raise ValueError("入力エラー" + str(inquiry))
#     return redirect('index')

def detail(request, id=None):
    toilet = Iotoiletapp.objects.get(floor_no = floor_no)
    return render(request, 'iotoiletapp/detail.html', {'toilet': toilet})

# def delete(request, id=None):
#     inquiry_id = get_object_or_404(Inquiry, pk=id)
#     inquiry_id.delete()
#     return redirect('index')

# def edit(request, id=None):
#     return HttpResponse("詳細:"+str(id))
