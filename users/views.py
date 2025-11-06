from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import User
from .serializers import UserSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status 
from faker import Faker
import random

@api_view(['POST'])
def createUser(request):
    
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def userList(request):
    
    users = User.objects.all()
    serializer = UserSerializer(users , many = True)
    
    return Response(serializer.data)

fake = Faker()

@api_view(['POST', 'GET'])
def generateUser(request):
    roles = ['employee', 'manager', 'hr','password']
    created_users = []

    for _ in range(20):
        data = {
            "username": fake.user_name() + str(random.randint(100, 999)),
            "email": fake.unique.email(),
            "role": random.choice(roles),
            "password": "password123"  # default password
        }

        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            created_users.append(serializer.data)

    return Response({
        "message": "20 users generated successfully",
        "users": created_users
    }, status=status.HTTP_201_CREATED)

