# Generated by Django 3.2.9 on 2021-12-02 07:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0006_alter_applicationmodel_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicationmodel',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 12, 2, 7, 31, 19, 876891)),
        ),
    ]
