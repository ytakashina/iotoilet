from django.db import models


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


class Sensor(models.Model):
    sensor_name = models.CharField("センサー名", max_length=20)
    sensor_no = models.IntegerField("センサー番号", default=-1)
    sensor_type_id = models.ForeignKey('SensorType', on_delete=models.CASCADE)
    sensor_status_type_id = models.ForeignKey('SensorStatusType', on_delete=models.CASCADE)
    toilet_id = models.ForeignKey('Toilet', on_delete=models.CASCADE)

    def __str__(self):
        return self.sensor_name


class SensorData(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    sensor_id = models.ForeignKey('Sensor', on_delete=models.CASCADE)
    sensor_data1 = models.CharField("センサーデータ1", max_length=20)
    sensor_data2 = models.CharField("センサーデータ2", max_length=20)
    sensor_data3 = models.CharField("センサーデータ3", max_length=20)
    sensor_data4 = models.CharField("センサーデータ4", max_length=20)
    sensor_data5 = models.CharField("センサーデータ5", max_length=20)

    class Meta:
        unique_together = (('timestamp', 'sensor_id'),)

    def __str__(self):
        return self.sensor_id


class Sex(models.Model):
    sex_name = models.CharField("性別名", max_length=20)
    sex_no = models.IntegerField("性別番号", default=1)

    def __str__(self):
        return self.sex_name
