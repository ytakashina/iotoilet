from django.db import models


class ToiletStatus(models.Model):
    timestamp = models.DateTimeField("登録時刻")
    toilet_id = models.ForeignKey('Toilet', on_delete=models.CASCADE)
    toilet_status_type_id = models.ForeignKey('toilet_status_type_id', on_delete=models.CASCADE)

    class Meta:
        unique_together = (('timestamp', 'toilet_id'),)

    def __str__(self):
        return self.timestamp


class ToiletStatusType(models.Model):
    toilet_status_type_name = models.CharField("個室状況名称", max_length=100)
    toilet_status_type_no = models.IntegerField("個室状況NO", default=-1)

    def __str__(self):
        return self.toilet_status_type_no


class Map(models.Model):
    map_name = models.CharField("地図名称", max_length=100)
    map_no = models.IntegerField("地図NO", default=-1)

    def __str__(self):
        return self.map_no


class Floor(models.Model):
    floor_name = models.CharField("フロア名", max_length=20)
    floor_no = models.IntegerField("フロア番号")

    def __str__(self):
        return self.floor_no


class User(models.Model):
    sex = models.ForeignKey('Sex', on_delete=models.CASCADE)
    floor_id = models.ForeignKey('Floor', on_delete=models.CASCADE)
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


class Room(models.Model):
    room_type_id = models.ForeignKey('Sex_room_type', on_delete=models.CASCADE)
    floor_id = models.ForeignKey('Floor', on_delete=models.CASCADE)
    room_name = models.CharField("個室名", max_length=20)
    room_no = models.IntegerField("個室番号", default=1)

    def __str__(self):
        return self.room_name


class Toilet(models.Model):
    room_id = models.ForeignKey('Room', on_delete=models.CASCADE)
    map_id = models.ForeignKey('Map', on_delete=models.CASCADE)
    toilet_name = models.CharField("トイレ名", max_length=20)
    toilet_no = models.IntegerField("トイレ番号", default=1)
    is_wheelchair = models.IntegerField("車いす", default=1)

    def __str__(self):
        return self.toilet_name

class SexRoomType(models.Model):
    room_type_id = models.ForeignKey('RoomType', on_delete=models.CASCADE)
    sex_id = models.ForeignKey('Sex', on_delete=models.CASCADE)

    class Meta:
        unique_together = (('room_type_id', 'sex_id'),)

    def __str__(self):
        return self.room_type_id

class ToiletStatsuHist(models.Model):
    toilet_name = models.CharField("トイレ名", max_length=20)
    toilet_no = models.IntegerField("トイレ番号", default=1)
    is_wheelchair = models.IntegerField("車いす", default=1)
    room_name = models.CharField("個室名", max_length=20)
    room_no = models.IntegerField("個室番号", default=1)
    floor_name = models.CharField("フロア名", max_length=20)
    floor_no = models.IntegerField("フロア番号")
    sex_name = models.CharField("性別名", max_length=20)
    sex_no = models.IntegerField("性別番号", default=1)
    map_name = models.CharField("地図名称", max_length=100)
    map_no = models.IntegerField("地図NO", default=-1)
    toilet_status_type_name = models.CharField("個室状況名称", max_length=100)
    toilet_status_type_no = models.IntegerField("個室状況NO", default=-1)
    timestamp = models.DateTimeField("登録時刻")

    def __str__(self):
        return self.toilet_name
