from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']


class LoginSerializer(serializers.Serializer):

    class Meta:
        username=serializers.EmailField()
        password=serializers.CharField()
