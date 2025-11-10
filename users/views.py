from django.shortcuts import render
from django.contrib.auth.hashers import check_password
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.permissions import IsAuthenticated

# Create your views here.
from rest_framework import generics
from .models import User
from .serializers import UserSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status 
from faker import Faker
from rest_framework.pagination import PageNumberPagination
import random


@api_view(['POST'])
@permission_classes([AllowAny]) 
def createUser(request):
    
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def userList(request):
    
    users = User.objects.all()
    serializer = UserSerializer(users , many = True)
    
    return Response(serializer.data)

fake = Faker()

@api_view(['POST', 'GET'])
@permission_classes([AllowAny])
def generateUser(request):
    roles = ['employee', 'manager', 'hr']
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

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def list_user_by_role(request,role):
    users = User.objects.filter(role = role)
    if not users.exists():
        return Response([], status=status.HTTP_200_OK)
    # serializer = UserSerializer(users,many = True)
    # return Response(serializer.data)
    paginator = PageNumberPagination()
    paginator.page_size = 5
    paginated_users = paginator.paginate_queryset(users,request)
    serializer = UserSerializer(paginated_users,many = True)
    return paginator.get_paginated_response(serializer.data)

@api_view(['POST'])
@permission_classes([AllowAny])  
def loginView(request):
    username = request.data.get('username')
    password = request.data.get('password')

    try:
        user = User.objects.get(username=username)
    except User.DoesNotExist:
        return Response({"error": "Invalid username or password"}, status=status.HTTP_400_BAD_REQUEST)

    # Manually check the password
    # Alvee's serializer uses make_password, so we use check_password
    if not check_password(password, user.password):
        return Response({"error": "Invalid username or password"}, status=status.HTTP_400_BAD_REQUEST)

    # If password is correct, get or create a token
    token, created = Token.objects.get_or_create(user=user)

    return Response({'token': token.key, 'user_id': user.id, 'username': user.username})


