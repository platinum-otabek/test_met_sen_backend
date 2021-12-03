from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view, permission_classes
from .models import SponsorModel, StudentModel, AllocateModel
from .serializers import SponserSerializer, StudentSerializer, PaymentSerializer, AllocateSerializer, \
    DashboardSerializer
from django.shortcuts import get_object_or_404
from .permissions import CustomAccessPermission
from django.db.models import Count, Sum


class SponsorView(APIView):
    permission_classes = [CustomAccessPermission]

    def get(self, request):
        all_sponsor = SponsorModel.objects.all()
        serializer = SponserSerializer(all_sponsor, many=True)
        return Response(data=serializer.data)


    @api_view(['GET', 'PATCH'])
    def get_one(request, pk):
        if request.method == 'GET':
            sponsor = get_object_or_404(SponsorModel, pk=pk)
            serializer = SponserSerializer(sponsor)
            return Response(serializer.data)
        if request.method == 'PATCH':
            data = JSONParser().parse(request)
            sponsor = get_object_or_404(SponsorModel, pk=pk)
            serializer = SponserSerializer(sponsor, data=data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=400)

    permission_classes = [CustomAccessPermission]

    def post(self, request):
        data = JSONParser().parse(request)
        serializer = SponserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)


class StudentView(APIView):
    permission_classes = [CustomAccessPermission]

    def get(self, request, format=None):
        print('get student')
        all_student = StudentModel.objects.all()
        serializer = StudentSerializer(all_student, many=True)
        return Response(data=serializer.data)

    permission_classes = [CustomAccessPermission]

    @api_view(['GET', 'PATCH'])
    def get_one(request, pk):
        if request.method == 'GET':
            student = get_object_or_404(StudentModel, pk=pk)
            serializer = StudentSerializer(student)
            return Response(serializer.data)
        if request.method == 'PATCH':
            data = JSONParser().parse(request)
            student = get_object_or_404(StudentModel, pk=pk)
            serializer = StudentSerializer(student, data=data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=400)

    permission_classes = [CustomAccessPermission]
    def post(self, request):
        data = JSONParser().parse(request)
        serializer = StudentSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)


class PaymentView(APIView):
    # permission_classes = [CustomAccessPermission]

    def post(self, request):
        data = JSONParser().parse(request)
        serializer = PaymentSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    @api_view(['GET'])
    def get_all_payment(request):
        all = SponsorModel.objects.annotate(
            all_count=Count('sponsors'),
            all_sum=Sum('sponsors__payment_money')
        )
        print(all)
        serializer = SponserSerializer(all.first())
        # data = serializers.serialize('json', list(all[0]), fields=('all_count', 'all_sum'))
        print(all[0].fullname, all[0].number, all[0].all_sum)
        return Response(data=serializer.data)


class AllocateView(APIView):
    # permission_classes = [CustomAccessPermission]

    def get(self, request):
        pass

    def post(self, request):
        data = JSONParser().parse(request)
        serializer = AllocateSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)


class DashboarView(APIView):
    permission_classes = [CustomAccessPermission]

    def get(self, request):
        all_paid_money = AllocateModel.objects.all().aggregate(Sum('money'))
        all_contracts = StudentModel.objects.all().aggregate(Sum('contract'))

        return Response(data={'all_paid_money': all_paid_money['money__sum'] or 0,
                              'all_contracts': all_contracts['contract__sum'] or 0})
