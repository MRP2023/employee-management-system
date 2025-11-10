from django.urls import path
from .views import userList, createUser, generateUser,list_user_by_role,loginView

urlpatterns = [
    path('login/', loginView),
    path('', userList),
    path('create', createUser),
    path('generate', generateUser),
    path('<str:role>/', list_user_by_role),

]
