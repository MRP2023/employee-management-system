from rest_framework import serializers
from . models import Employee
from users.models import User


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'

class UserEmployeeDetailSerializer(serializers.Serializer):
    username = serializers.CharField(source ="user.username")
    email = serializers.EmailField(source ="user.email")
    role = serializers.CharField(source ="user.role")
    full_name = serializers.CharField()
    phone_number = serializers.CharField()
    department = serializers.CharField()
    designation = serializers.CharField()
    join_date = serializers.DateField()
    salary = serializers.DecimalField(max_digits=10, decimal_places=2)