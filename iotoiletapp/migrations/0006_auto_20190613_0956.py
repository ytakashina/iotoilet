# Generated by Django 2.2.1 on 2019-06-13 00:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('iotoiletapp', '0005_auto_20190612_1642'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sensordata',
            name='timestamp',
            field=models.DateTimeField(),
        ),
    ]
