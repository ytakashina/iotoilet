from django.db import models


class ToiletStatus(models.Model):
    timestamp = models.DateTimeField("登録時刻")
    toilet_id = models.ForeignKey('Toilet', on_delete=models.PROTECT)
    toilet_status_type_id = models.ForeignKey('ToiletStatusType', on_delete=models.PROTECT)

    class Meta:
        unique_together = (('timestamp', 'toilet_id'),)

    def __str__(self):
        return str(self.timestamp)


class ToiletStatusType(models.Model):
    toilet_status_type_name = models.CharField("個室状況名称", max_length=20)
    toilet_status_type_no = models.IntegerField("個室状況番号", default=-1)

    def __str__(self):
        return self.toilet_status_type_name


class Map(models.Model):
    map_name = models.CharField("地図名称", max_length=20)
    map_no = models.IntegerField("地図番号", default=-1)

    def __str__(self):
        return self.map_name


class Floor(models.Model):
    floor_name = models.CharField("フロア名", max_length=20)
    floor_no = models.IntegerField("フロア番号")

    def __str__(self):
        return self.floor_name


class User(models.Model):
    sex = models.ForeignKey('Sex', on_delete=models.SET_NULL, null=True)
    floor_id = models.ForeignKey('Floor', on_delete=models.SET_NULL, null=True)
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
    sensor_type_id = models.ForeignKey('SensorType', on_delete=models.SET_NULL, null=True)
    sensor_status_type_id = models.ForeignKey('SensorStatusType', on_delete=models.SET_NULL, null=True)
    toilet_id = models.ForeignKey('Toilet', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.sensor_name


class SensorData(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    sensor_id = models.ForeignKey('Sensor', on_delete=models.PROTECT)
    value1 = models.CharField("センサー値1", max_length=20, blank=True)
    value2 = models.CharField("センサー値2", max_length=20, blank=True)
    value3 = models.CharField("センサー値3", max_length=20, blank=True)
    value4 = models.CharField("センサー値4", max_length=20, blank=True)
    value5 = models.CharField("センサー値5", max_length=20, blank=True)

    class Meta:
        unique_together = (('timestamp', 'sensor_id'),)

    def __str__(self):
        return str(self.sensor_id)


class Sex(models.Model):
    sex_name = models.CharField("性別名", max_length=20)
    sex_no = models.IntegerField("性別番号", default=-1)

    def __str__(self):
        return self.sex_name


class SexRoomType(models.Model):
    room_type_id = models.ForeignKey("RoomType", on_delete=models.CASCADE)
    sex_id = models.ForeignKey("Sex", on_delete=models.CASCADE)
    sex_room_type_name = models.CharField("性別個室対応名", max_length=20, null=True)

    class Meta:
        unique_together = (('room_type_id', 'sex_id'),)

    def __str__(self):
        return self.sex_room_type_name


class RoomType(models.Model):
    room_type_name = models.CharField("個室タイプ", max_length=20)
    room_type_no = models.IntegerField("個室タイプ番号", default=-1)

    def __str__(self):
        return self.room_type_name


class Room(models.Model):
    room_type_id = models.ForeignKey('RoomType', on_delete=models.SET_NULL, null=True)
    floor_id = models.ForeignKey('Floor', on_delete=models.PROTECT)
    room_name = models.CharField("個室名", max_length=20)
    room_no = models.IntegerField("個室番号", default=-1)

    def __str__(self):
        return self.room_name


class Toilet(models.Model):
    room_id = models.ForeignKey('Room', on_delete=models.PROTECT)
    map_id = models.ForeignKey('Map', on_delete=models.SET_NULL, null=True)
    toilet_name = models.CharField("トイレ名", max_length=20)
    toilet_no = models.IntegerField("トイレ番号", default=-1)
    is_wheelchair = models.IntegerField("車いす", default=1)
    brightness_threshold = models.IntegerField("明るさ閾値", default=1)

    def __str__(self):
        return self.toilet_name


class ToiletStatsuHist(models.Model):
    toilet_name = models.CharField("トイレ名", max_length=20)
    toilet_no = models.IntegerField("トイレ番号", default=-1)
    is_wheelchair = models.IntegerField("車いす", default=-1)
    room_name = models.CharField("個室名", max_length=20)
    room_no = models.IntegerField("個室番号", default=-1)
    floor_name = models.CharField("フロア名", max_length=20)
    floor_no = models.IntegerField("フロア番号")
    sex_name = models.CharField("性別名", max_length=20)
    sex_no = models.IntegerField("性別番号", default=-1)
    map_name = models.CharField("地図名称", max_length=20)
    map_no = models.IntegerField("地図番号", default=-1)
    toilet_status_type_name = models.CharField("個室状況名称", max_length=20)
    toilet_status_type_no = models.IntegerField("個室状況番号", default=-1)
    timestamp = models.DateTimeField("登録時刻")

    def __str__(self):
        return self.toilet_name