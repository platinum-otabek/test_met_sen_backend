from rest_framework import serializers
from django.db.models import Count, Sum
from app.models import SponsorModel, StudentModel, PaymentModel, AllocateModel


class SponserSerializer(serializers.ModelSerializer):
    all_sum = serializers.SerializerMethodField()
    remain_sum = serializers.SerializerMethodField()

    class Meta:
        model = SponsorModel
        fields = ('fullname', 'number', 'status', 'type_user', 'organization_name', 'all_sum', 'remain_sum')

    def get_all_sum(self, obj):
        all = SponsorModel.objects.filter(pk=obj.pk).annotate(
            all_sum=Sum('sponsors__payment_money')
        )
        return all[0].all_sum or 0

    def get_remain_sum(self, obj):
        allocate = AllocateModel.objects.filter(student_id=obj.pk).aggregate(Sum('money'))
        return allocate['money__sum'] or 0

    def create(self, validated_data):
        sponsor = SponsorModel.objects.create(**validated_data)
        return sponsor

    def update(self, instance, validated_data):
        instance.fullname = validated_data['fullname']
        instance.number = validated_data['number']
        instance.type_user = validated_data['type_user']
        instance.organization_name = validated_data.get('organization_name', '')
        instance.save()
        return instance


class StudentSerializer(serializers.ModelSerializer):
    paid = serializers.SerializerMethodField()

    class Meta:
        model = StudentModel
        fields = '__all__'

    def get_paid(self, obj):
        allocate = AllocateModel.objects.filter(student_id=obj.pk).aggregate(Sum('money'))
        return allocate['money__sum'] or 0

    def create(self, validated_data):
        student = StudentModel.objects.create(**validated_data)
        return student


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentModel
        fields = '__all__'

    def create(self, validated_data):
        payment = PaymentModel.objects.create(**validated_data)
        return payment


class DashboardSerializer(serializers.Serializer):
    paid_money = serializers.SerializerMethodField(read_only=False)
    all_contracts = serializers.SerializerMethodField()

    def get_paid_money(self):
        all_paid_money = AllocateModel.objects.all().aggregate(Sum('money'))
        return all_paid_money['money__sum'] or 0

    def get_all_contracts(self):
        all_contracts = StudentModel.objects.all().aggregate(Sum('contract'))
        return all_contracts['contract__sum'] or 0


class AllocateSerializer(serializers.ModelSerializer):
    class Meta:
        model = AllocateModel
        fields = '__all__'

    def validate(self, attrs):
        sponsor_pk = attrs['sponsor'].pk
        student_pk = attrs['student'].pk
        sponsor = SponsorModel.objects.filter(pk=sponsor_pk).annotate(
            all_sum=Sum('sponsors__payment_money')
        )
        allocated_sponsor_sum = AllocateModel.objects.filter(sponsor_id=sponsor_pk).aggregate(Sum('money'))
        allocated_sum = AllocateModel.objects.filter(student_id=student_pk).aggregate(Sum('money'))
        # sponsor[0].all_sum -> all sending money(payments)
        # allocated_sum -> separated tum to student
        # first is check contract sum
        student = StudentModel.objects.filter(pk=student_pk).first()
        if int(allocated_sum['money__sum'] or 0) + attrs['money'] > student.contract:
            raise serializers.ValidationError(detail='This students does not need money')
        # second check sponsor money
        if int(sponsor[0].all_sum or 0) - int(allocated_sponsor_sum['money__sum'] or 0) < attrs['money']:
            raise serializers.ValidationError('Sponsor does not have this money')
        return attrs

    def create(self, validated_data):
        instance = AllocateModel.objects.create(**validated_data)
        return instance
