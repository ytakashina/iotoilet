from django.db import models

# Create your models here.


class Sex(models.Model):
    sex_name = models.CharField("性別名", max_length=20)
    sex_no = models.IntegerField("性別", default=1)
  
    def __str__(self):
        return self.sex_name
