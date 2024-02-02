from rest_framework import serializers
from rest_framework.authtoken.models import Token
from .models import Users, Events

class EventsSerializer(serializers.ModelSerializer):
    author = serializers.PrimaryKeyRelatedField(read_only=True)
    
    class Meta:
        model = Events
        fields = '__all__'

class UsersSerializer(serializers.ModelSerializer):
    events = EventsSerializer(many=True,read_only=True)

    class Meta:
        model = Users
        fields = '__all__'
        extra_kwargs = {'password': {'write_only': True}}
    
    def create(self, validated_data):
        user = Users(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        Token.objects.create(user=user)
        return user