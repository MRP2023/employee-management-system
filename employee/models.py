from django.db import models
from users.models import User
# Create your models here.

class Employee(models.Model):
    
    user = models.OneToOneField(User, on_delete=models.CASCADE, elated_name='employee_profile')

    full_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    department = models.CharField(max_length=100, blank=True, null=True)
    designation = models.CharField(max_length=100, blank=True, null=True)
    join_date = models.DateField(blank=True, null=True)
    salary = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return f"{self.full_name} ({self.user.username})"
