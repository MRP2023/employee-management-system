from rest_framework import serializers
from .models import AttendanceRecord, LeaveRequest

class AttendanceRecordSerializer(serializers.ModelSerializer):
    employee_name = serializers.CharField(source='employee.user.get_full_name', read_only=True)
    class Meta:
        model = AttendanceRecord
        fields = ['id', 'employee', 'employee_name', 'date', 'check_in', 'check_out', 'status']
        read_only_fields = ['employee', 'date', 'status']


class LeaveRequestSerializer(serializers.ModelSerializer):
    employee_name = serializers.CharField(source='employee.user.get_full_name', read_only=True)
    class Meta:
        model = LeaveRequest
        fields = ['id', 'employee', 'employee_name', 'start_date', 'end_date', 'reason', 'status', 'requested_on', 'approved_by']
        read_only_fields = ['employee', 'status', 'approved_by', 'requested_on'] 