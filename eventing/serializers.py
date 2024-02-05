from rest_framework import serializers
from rest_framework.authtoken.models import Token
from .models import Events

class EventsSerializer(serializers.ModelSerializer):
    author = serializers.PrimaryKeyRelatedField(read_only=True)
    
    class Meta:
        model = Events
        fields = '__all__'