from rest_framework import serializers
from .models import Users, Events

class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = '__all__'
        extra_kwargs = {'password': {'write_only': True}}

class EventsSerializer(serializers.ModelSerializer):
    author = UsersSerializer(many=False,read_only=True)
    
    class Meta:
        model = Events
        fields = '__all__'