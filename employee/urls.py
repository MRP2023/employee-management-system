from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EmployeeViewSet,EmployeeDetailByUserView


router = DefaultRouter()
router.register('', EmployeeViewSet , basename='employee')

urlpatterns = [
    path('details/<int:user_id>', EmployeeDetailByUserView.as_view(), name='employee-detail-by-user'),
    path('',include(router.urls))
    
]
