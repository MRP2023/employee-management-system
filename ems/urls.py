
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('departments/', include('departments.urls')),
    # path('employee/', include('employee.urls')),
    path('attendance/', include('attendance.urls')), 
    path('api-auth/', include('rest_framework.urls')),
]

