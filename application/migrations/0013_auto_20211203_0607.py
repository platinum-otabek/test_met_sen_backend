# Generated by Django 3.2.9 on 2021-12-03 06:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0012_alter_applicationmodel_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='applicationmodel',
            name='organization_name',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='applicationmodel',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 12, 3, 6, 7, 35, 590816)),
        ),
    ]
