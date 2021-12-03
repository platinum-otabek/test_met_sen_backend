import datetime

from django.db import models


# Create your models here.


class ApplicationModel(models.Model):
    TYPE_PERSON = (
        ('jismoniy_shaxs', 'jismoniy shaxs'),
        ('yuridik_shaxs', 'yuridik shaxs')
    )
    TYPE_STATUS = (
        ('accept', 'accept'),
        ('reject', 'reject'),
        ('moderation', 'moderation'),
        ('new', 'new')
    )
    fullname = models.CharField(max_length=155)
    number = models.CharField(max_length=13)
    sum = models.IntegerField()
    type_person = models.CharField(max_length=30, choices=TYPE_PERSON)
    date = models.DateTimeField(default=datetime.datetime.now())
    status = models.CharField(max_length=31, default='new', choices=TYPE_STATUS)
    organization_name = models.CharField(max_length=255, default='')
