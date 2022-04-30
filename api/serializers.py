from rest_framework import serializers
from base.models import User, Project, IP

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email']

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['name']

class IPSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['ipAdress']