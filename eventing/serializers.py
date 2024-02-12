from rest_framework import serializers
from rest_framework.authtoken.models import Token
from .models import Events, Tasks

class TasksSerializer(serializers.ModelSerializer):
    event = serializers.PrimaryKeyRelatedField(read_only=True)
    
    class Meta:
        model = Tasks
        fields = '__all__'

class EventsSerializer(serializers.ModelSerializer):
    author = serializers.PrimaryKeyRelatedField(read_only=True)
    tasks = TasksSerializer(many=True,read_only=True)
    
    class Meta:
        model = Events
        fields = '__all__'