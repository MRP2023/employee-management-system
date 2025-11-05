from django.urls import path
from .views import userList, createUser, generateUser

urlpatterns = [
    path('', userList),
    path('create', createUser),
    path('generate', generateUser)
]
