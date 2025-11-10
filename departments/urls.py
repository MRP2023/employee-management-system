from django.urls import path
from . import views

urlpatterns = [
    # Department URLs
    path('', views.department_list_create, name='department-list-create'),
    path('<int:pk>/', views.department_detail, name='department-detail'),
    
    # Designation URLs
    path('designations/', views.designation_list_create, name='designation-list-create'),
    path('designations/<int:pk>/', views.designation_detail, name='designation-detail'),
]