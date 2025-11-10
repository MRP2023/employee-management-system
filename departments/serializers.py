from rest_framework import serializers
from .models import Department, Designation # Import new model

# Updated DepartmentSerializer
class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        # Add parent_department to fields
        fields = ['id', 'name', 'description', 'manager', 'parent_department']

# New Serializer for Designation
class DesignationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Designation
        fields = ['id', 'title', 'description', 'department']