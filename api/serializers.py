from rest_framework import serializers
from base.models import User, Project, IP

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'

class IPSerializer(serializers.ModelSerializer):
    class Meta:
        model = IP
        fields = '__all__'