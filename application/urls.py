from django.urls import path
from .views import ApplicationView, ApplicationUpdateView

urlpatterns = [
    path('', ApplicationView.as_view()),
    path('<int:pk>/', ApplicationUpdateView.as_view())
]
