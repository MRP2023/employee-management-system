from django.db import models
from django.conf import settings

# Create your models here.
class Department(models.Model):
    name = models.CharField(max_length=100, unique=True, help_text="Name of the department")
    description = models.TextField(blank=True, null=True, help_text="Optional description")
    
    # Links to the manager (a User)
    manager = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='managed_department',
        help_text="The manager of this department"
    )
    
    # New field for hierarchical departments (e.g., "Engineering" > "Frontend")
    parent_department = models.ForeignKey(
        'self',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='sub_departments'
    )

    def __str__(self):
        return self.name

# New Model for Designations
class Designation(models.Model):
    title = models.CharField(max_length=100, unique=True) 
    description = models.TextField(blank=True, null=True)
    
    # Link to a department
    department = models.ForeignKey(
        Department,
        on_delete=models.CASCADE, # If department is deleted, delete this title
        related_name='designations'
    )

    def __str__(self):
        return f"{self.title} ({self.department.name})"