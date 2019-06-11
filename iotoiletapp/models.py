from django.db import models

# Create your models here.

class ToiletStatus(models.Model):

    timestamp = models.DateTimeField("登録時刻")
    toilet_id = models.CharField("個室ID", max_length=20)
    toilet_status_type_id = models.ForeignKey('toilet_status_type_id', on_delete=models.CASCADE)

    def __str__(self):
        return [self.timestamp, self.toilet_id]


class ToiletStatusType(models.Model):

    toilet_status_type_id = models.CharField("個室状況ID", max_length=20)
    toilet_status_type_name = models.CharField("個室状況名称", max_length=100)
    toilet_status_type_name = models.IntegerField("個室状況NO", default=-1)

    def __str__(self):
        return self.toilet_status_type_id
