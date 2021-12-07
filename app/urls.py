from django.urls import path
from app.views import SponsorView, StudentView, PaymentView, AllocateView, DashboarView, \
    SponsorRetriveUpdateDestroyView, StudentRetriveUpdateDestroyView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('sponsor/', SponsorView.as_view()),
    path('sponsor/<int:pk>/', SponsorRetriveUpdateDestroyView.as_view()),

    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('student/', StudentView.as_view()),
    path('student/<int:pk>/', StudentRetriveUpdateDestroyView.as_view()),

    path('payment/', PaymentView.as_view()),
    # path('all_payment/', PaymentView.get_all_payment),

    path('allocate/', AllocateView.as_view()),

    path('dashboard/', DashboarView.as_view())

]
