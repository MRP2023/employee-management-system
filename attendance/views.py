# attendance/views.py
from rest_framework import viewsets, views, permissions, status
from rest_framework.response import Response
from django.utils import timezone
from .models import AttendanceRecord, LeaveRequest
from .serializers import AttendanceRecordSerializer, LeaveRequestSerializer

class AttendanceLogViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint for viewing Attendance Logs.
    Managers can see all logs. Employees can only see their own.
    """
    queryset = AttendanceRecord.objects.all()
    serializer_class = AttendanceRecordSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.is_staff or user.is_superuser: # Assuming managers are staff
            return AttendanceRecord.objects.all()
        # Assumes user is linked to an Employee
        return AttendanceRecord.objects.filter(employee__user=user)

class LeaveRequestViewSet(viewsets.ModelViewSet):
    """
    API endpoint for creating and managing Leave Requests.
    Employees can create/view their own. Managers can view/approve all.
    """
    queryset = LeaveRequest.objects.all()
    serializer_class = LeaveRequestSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.is_staff or user.is_superuser:
            return LeaveRequest.objects.all()
        return LeaveRequest.objects.filter(employee__user=user)

    def perform_create(self, serializer):
        # Automatically set the employee when a request is created
        serializer.save(employee=self.request.user.employee)

# --- Action Views for Check-in / Check-out ---

class CheckInView(views.APIView):
    """
    API endpoint for an employee to check-in.
    """
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        employee = request.user.employee
        today = timezone.now().date()
        
        # Get or create the record for today
        record, created = AttendanceRecord.objects.get_or_create(
            employee=employee, 
            date=today
        )
        
        if record.check_in:
            return Response(
                {"error": "You have already checked in today."}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        
        record.check_in = timezone.now().time()
        record.status = 'PRESENT'
        record.save()
        
        serializer = AttendanceRecordSerializer(record)
        return Response(serializer.data, status=status.HTTP_200_OK)

class CheckOutView(views.APIView):
    """
    API endpoint for an employee to check-out.
    """
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        employee = request.user.employee
        today = timezone.now().date()
        
        try:
            record = AttendanceRecord.objects.get(employee=employee, date=today)
        except AttendanceRecord.DoesNotExist:
            return Response(
                {"error": "You have not checked in today."}, 
                status=status.HTTP_400_BAD_REQUEST
            )

        if not record.check_in:
            return Response(
                {"error": "You have not checked in today."}, 
                status=status.HTTP_400_BAD_REQUEST
            )

        if record.check_out:
            return Response(
                {"error": "You have already checked out today."}, 
                status=status.HTTP_400_BAD_REQUEST
            )

        record.check_out = timezone.now().time()
        record.save()
        
        serializer = AttendanceRecordSerializer(record)
        return Response(serializer.data, status=status.HTTP_200_OK)
