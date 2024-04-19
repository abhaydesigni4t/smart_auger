from rest_framework import serializers
from .models import Location

class DataManageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # Exclude 'timestamp' field when posting data
        if self.context.get('request') and self.context['request'].method == 'POST':
            self.fields.pop('timestamp', None)

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()