from rest_framework import serializers
from .models import Location

class DataManageSerializer(serializers.ModelSerializer):
    timestamp = serializers.DateTimeField(read_only=True)

    class Meta:
        model = Location
        exclude = []

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()