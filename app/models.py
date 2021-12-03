import datetime

from django.db import models


# Create your models here.

class SponsorModel(models.Model):
    TYPE_STATUS = (
        ('accept', 'accept'),
        ('reject', 'reject'),
        ('moderation', 'moderation'),
        ('new', 'new')
    )
    TYPE_PERSON = (
        ('jismoniy_shaxs', 'jismoniy shaxs'),
        ('yuridik_shaxs', 'yuridik shaxs')
    )
    fullname = models.CharField(max_length=155)
    number = models.CharField(max_length=13)
    status = models.CharField(max_length=31, default='new', choices=TYPE_STATUS)
    type_user = models.CharField(max_length=255, choices=TYPE_PERSON)
    organization_name = models.CharField(max_length=255, default='')


class PaymentModel(models.Model):
    payment_money = models.IntegerField()
    payment_type = models.CharField(max_length=255)
    sponsor = models.ForeignKey(SponsorModel, on_delete=models.DO_NOTHING, related_name='sponsors')
    date = models.DateTimeField(default=datetime.datetime.now())


class StudentModel(models.Model):
    fullname = models.CharField(max_length=255)
    number = models.CharField(max_length=13)
    university = models.CharField(max_length=255)
    type_student = models.CharField(max_length=255)
    contract = models.IntegerField()


class AllocateModel(models.Model):
    sponsor = models.ForeignKey(SponsorModel, on_delete=models.DO_NOTHING, related_name='sponsors_allocate')
    student = models.ForeignKey(StudentModel, on_delete=models.DO_NOTHING, related_name='students_allocate')
    money = models.IntegerField()
    date = models.DateTimeField(default=datetime.datetime.now())
