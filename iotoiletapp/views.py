from django.shortcuts import render, get_object_or_404, redirect #追加
from django.http import HttpResponse
from iotoiletapp.models import Toilet, Room, ToiletStatus
from iotoiletapp.forms import IotoiletappForm

#一覧
def index(request):
    toilet_status = ToiletStatus.objects.row().order_by('floor_no') # 値を取得
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
