from django.shortcuts import render
from rest_framework import viewsets,generics,permissions
from rest_framework.exceptions import NotFound
from rest_framework.response import Response
from .models import Employee
from . models import User
from .serializers import EmployeeSerializer, UserEmployeeDetailSerializer

# Create your views here.


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    
    
class EmployeeDetailByUserView(generics.GenericAPIView):
    serializer_class = UserEmployeeDetailSerializer
    permission_classes = [permissions.IsAuthenticated]

    

    def get(self, request, user_id):
        try:
            user = User.objects.get(id = user_id)
        except User.DoesNotExist:
            raise NotFound("User Not Found")
        
        try:
            employee = user.employee_profile
        except Employee.DoesNotExist:
            raise NotFound("Employee Profile Not Found nnnnn")
        
        serializer = self.serializer_class(employee)
        return Response(serializer.data)
