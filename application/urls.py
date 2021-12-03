from django.urls import path
from .views import ApplicationView

urlpatterns = [
    path('', ApplicationView.as_view(), name='get_application'),
    path('update_status/<int:pk>/', ApplicationView.update_status, name='application_update')
]
