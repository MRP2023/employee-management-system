from django.urls import path
from .views import UserListCreateAPI

urlpatterns = [
    path('users/', UserListCreateAPI.as_view(), name='user-list-create'),
]
