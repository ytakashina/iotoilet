from django.db import models

# Create your models here.

class Floor(models.Model):
    floor_name = (
        (1, "25階"),
        (2, "26階"),
        (3, "27階"),
        (4, "28階"),
        (5, "29階"),
    )
    floor_no = models.IntegerField("フロアNo.")

class User(models.Model):
    sex = models.ForeignKey('Sex', on_delete=models.CASCADE)
    floor_id = models.ForeignKey('Floor', on_delete=models.CASCADE)
    user_id = models.CharField("ユーザID", max_length=20)
    password = models.CharField("パスワード", max_length=20)
    user_name = models.CharField("ユーザ名", max_length=20)

    def __str__(self):
        return self.user_name