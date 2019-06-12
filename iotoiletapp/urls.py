from django.urls import path
from inquiry import views

urlpatterns = [
    path('', views.index, name='index'),
    path('search/', views.add, name='search'),
    # path('save/', views.save, name='save'),
    # path('edit/<int:id>', views.edit, name='edit'),
    # path('delete/<int:id>', views.delete, name='delete'),
    # path('detail/<int:id>', views.detail, name='detail'),
# 1          ↑-------------------------------------←
# 2          →-------------------↑
]