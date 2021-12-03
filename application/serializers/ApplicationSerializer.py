from rest_framework import serializers
import datetime
from application.models import ApplicationModel


class ApplicationSerializer(serializers.Serializer):
    fullname = serializers.CharField(max_length=155)
    number = serializers.CharField(max_length=13)
    sum = serializers.IntegerField()
    type_person = serializers.CharField(max_length=30, )
    date = serializers.DateTimeField(default=datetime.datetime.now())
    status = serializers.CharField(max_length=31, default='new', )

    def create(self, validated_data):
        application = ApplicationModel(
            fullname=validated_data['fullname'],
            number=validated_data['number'],
            sum=validated_data['sum'],
            type_person=validated_data['type_person'],
        )
        application.save()
        return application

    def update(self, instance, validated_data):
        instance.status = validated_data['status']
        instance.save()
        return instance
