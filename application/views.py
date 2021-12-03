from rest_framework.views import APIView
from application.models import ApplicationModel
from application.serializers.ApplicationSerializer import ApplicationSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view


class ApplicationView(APIView):
    def get(self, request):
        all_applications = ApplicationModel.objects.all()
        serializer_applications = ApplicationSerializer(data=all_applications, many=True)
        serializer_applications.is_valid()
        return Response(data=serializer_applications.data)

    def post(self, request):
        application = ApplicationSerializer(data=request.data)
        application.is_valid(raise_exception=True)
        application.save()
        return Response(data=application.data, status=status.HTTP_201_CREATED)

    @api_view(['PATCH'])
    def update_status(request, pk):
        if request.method == 'PATCH':
            try:
                ApplicationModel.objects.filter(pk=pk) \
                    .update(status=request.data['status'])
                return Response({'message': 'success'})
            except Exception as e:
                print(e)
                return Response({'message': e})
