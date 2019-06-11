from django.db import models

<<<<<<< HEAD
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
=======

class Floor(models.Model):
    floor_name = models.CharField("フロア名", max_length=20)
    floor_no = models.IntegerField("フロア番号")

    def __str__(self):
        return self.floor_no


class User(models.Model):
    sex = models.ForeignKey('性別', on_delete=models.CASCADE)
    floor_id = models.ForeignKey('フロアID', on_delete=models.CASCADE)
    user_id = models.CharField("ユーザID", max_length=20)
    password = models.CharField("パスワード", max_length=20)
    user_name = models.CharField("ユーザ名", max_length=20)

    def __str__(self):
        return self.user_name


class SensorStatusType(models.Model):
    sensor_status_type_name = models.CharField("センサー状態タイプ名", max_length=20)
    sensor_status_type_no = models.IntegerField("センサー状態タイプ番号", default=-1)

    def __str__(self):
        return self.sensor_status_type_name


class SensorType(models.Model):
    sensor_type_name = models.CharField("センサータイプ名", max_length=20)
    sensor_type_no = models.IntegerField("センサータイプ番号", default=-1)

    def __str__(self):
        return self.sensor_type_name


class Sex(models.Model):
    sex_name = models.CharField("性別名", max_length=20)
    sex_no = models.IntegerField("性別番号", default=1)
  
    def __str__(self):
        return self.sex_name
>>>>>>> master
