from django.db import models
from users.models import User
from departments.models import Department, Designation
# Create your models here.

class Employee(models.Model):
    
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='employee_profile')
    full_name = models.CharField(max_length=100,blank=True, null=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, blank=True, null=True,related_name='employees')
    designation = models.ForeignKey(Designation,on_delete=models.SET_NULL, blank=True, null=True,related_name='employees')
    join_date = models.DateField(blank=True, null=True)
    salary = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return f"{self.full_name} ({self.user.username})"
