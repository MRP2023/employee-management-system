from rest_framework import serializers
from .models import User
from django.contrib.auth.hashers import make_password

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'role','password']
        extra_kwargs = {
            'password' : {'write_only' : True} 
        }

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        if password is not None:
            validated_data['password'] = make_password(password)

        return super().create(validated_data)
    

    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)
        if password is not None:
            instance.password  = make_password(password)

        return super().update(instance, validated_data)