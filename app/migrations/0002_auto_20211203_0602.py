# Generated by Django 3.2.9 on 2021-12-03 06:02

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='allocatemodel',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 12, 3, 6, 2, 52, 621498)),
        ),
        migrations.AlterField(
            model_name='paymentmodel',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 12, 3, 6, 2, 52, 620696)),
        ),
    ]