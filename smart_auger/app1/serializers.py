from rest_framework import serializers
from .models import data_management_model

class DataManageSerializer(serializers.ModelSerializer):
    timestamp = serializers.DateTimeField(read_only=True)

    class Meta:
        model = data_management_model
        exclude = []