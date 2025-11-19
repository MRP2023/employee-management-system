from django.contrib import admin
from .models import Department, Designation # Import new model

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'manager', 'parent_department')
    list_filter = ('name',)
    search_fields = ('name', 'manager__username')
    
    # To make selecting parent easier
    autocomplete_fields = ['manager', 'parent_department']

# New Admin for Designations
@admin.register(Designation)
class DesignationAdmin(admin.ModelAdmin):
    list_display = ('title', 'department')
    list_filter = ('department',)
    search_fields = ('title', 'department__name')
    autocomplete_fields = ['department']