from rest_framework.response import Response
from .models import SponsorModel, StudentModel, AllocateModel, PaymentModel
from .serializers import SponserSerializer, StudentSerializer, PaymentSerializer, AllocateSerializer
from .permissions import CustomAccessPermission
from django.db.models import Count, Sum
from rest_framework import generics


class SponsorView(generics.ListCreateAPIView):
    permission_classes = [CustomAccessPermission]
    queryset = SponsorModel.objects.all()
    serializer_class = SponserSerializer


class SponsorRetriveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [CustomAccessPermission]
    queryset = SponsorModel.objects.all()
    serializer_class = SponserSerializer

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)


class StudentView(generics.ListCreateAPIView):
    permission_classes = [CustomAccessPermission]
    queryset = StudentModel.objects.all()
    serializer_class = StudentSerializer


class StudentRetriveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [CustomAccessPermission]
    queryset = StudentModel.objects.all()
    serializer_class = StudentSerializer

    def put(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)


class PaymentView(generics.ListCreateAPIView):
    permission_classes = [CustomAccessPermission]
    queryset = PaymentModel.objects.all()
    serializer_class = PaymentSerializer

    def get(self, request, *args, **kwargs):
        all = SponsorModel.objects.annotate(
            all_count=Count('sponsors'),
            all_sum=Sum('sponsors__payment_money')
        )
        serializer = SponserSerializer(all.first())
        return Response(data=serializer.data)


class AllocateView(generics.CreateAPIView):
    permission_classes = [CustomAccessPermission]
    queryset = AllocateModel.objects.all()
    serializer_class = AllocateSerializer


class DashboarView(generics.ListAPIView):
    permission_classes = [CustomAccessPermission]

    def get(self, request, *args, **kwargs):
        all_paid_money = AllocateModel.objects.all().aggregate(Sum('money'))
        all_contracts = StudentModel.objects.all().aggregate(Sum('contract'))

        return Response(data={'all_paid_money': all_paid_money['money__sum'] or 0,
                              'all_contracts': all_contracts['contract__sum'] or 0})
