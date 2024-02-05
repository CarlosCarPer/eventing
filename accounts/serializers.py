from rest_framework import serializers
from rest_framework.authtoken.models import Token
from .models import Users
from eventing.serializers import EventsSerializer

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