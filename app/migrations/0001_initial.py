# Generated by Django 3.2.9 on 2021-12-03 06:00

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SponsorModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=155)),
                ('number', models.CharField(max_length=13)),
                ('status', models.CharField(choices=[('accept', 'accept'), ('reject', 'reject'), ('moderation', 'moderation'), ('new', 'new')], default='new', max_length=31)),
                ('type_user', models.CharField(choices=[('jismoniy_shaxs', 'jismoniy shaxs'), ('yuridik_shaxs', 'yuridik shaxs')], max_length=255)),
                ('organization_name', models.CharField(default='', max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='StudentModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=255)),
                ('number', models.CharField(max_length=13)),
                ('university', models.CharField(max_length=255)),
                ('type_student', models.CharField(max_length=255)),
                ('contract', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='PaymentModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_money', models.IntegerField()),
                ('payment_type', models.CharField(max_length=255)),
                ('date', models.DateTimeField(default=datetime.datetime(2021, 12, 3, 6, 0, 43, 480716))),
                ('sponsor', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='sponsors', to='app.sponsormodel')),
            ],
        ),
        migrations.CreateModel(
            name='AllocateModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('money', models.IntegerField()),
                ('date', models.DateTimeField(default=datetime.datetime(2021, 12, 3, 6, 0, 43, 481542))),
                ('sponsor', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='sponsors_allocate', to='app.sponsormodel')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='students_allocate', to='app.studentmodel')),
            ],
        ),
    ]