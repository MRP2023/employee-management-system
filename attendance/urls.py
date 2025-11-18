# attendance/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    AttendanceLogViewSet, 
    LeaveRequestViewSet, 
    CheckInView, 
    CheckOutView
)

router = DefaultRouter()
router.register(r'logs', AttendanceLogViewSet, basename='attendance-log')
router.register(r'leave-requests', LeaveRequestViewSet, basename='leave-request')

urlpatterns = [
    path('', include(router.urls)),
    path('check-in/', CheckInView.as_view(), name='check-in'),
    path('check-out/', CheckOutView.as_view(), name='check-out'),
]