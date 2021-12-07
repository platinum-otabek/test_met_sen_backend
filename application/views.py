from application.models import ApplicationModel
from application.serializers.ApplicationSerializer import ApplicationSerializer
from rest_framework import generics


class ApplicationView(generics.ListCreateAPIView):
    queryset = ApplicationModel.objects.all()
    serializer_class = ApplicationSerializer


class ApplicationUpdateView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ApplicationModel.objects.all()
    serializer_class = ApplicationSerializer
