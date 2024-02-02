from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import PermissionDenied
from .serializers import EventsSerializer, UsersSerializer
from .models import Events

def index(request):
    return Response("Hello, world. You're at the polls index.")

class EventsList(ListCreateAPIView):
    queryset = Events.objects.all()
    serializer_class = EventsSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class EventsDetail(RetrieveUpdateDestroyAPIView):
    queryset = Events.objects.all()
    serializer_class = EventsSerializer

    def delete(self, request, *args, **kwargs):
        event = Events.objects.get(pk=self.kwargs["pk"])
        if not request.user == event.author:
            raise PermissionDenied("You can not delete this event.")
        return super().delete(request, *args, **kwargs)

class UsersCreate(CreateAPIView):
    authentication_classes = ()
    permission_classes = ()
    serializer_class = UsersSerializer

class LoginView(APIView):
    permission_classes = ()

    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(username=username, password=password)
        if user:
            return Response({"token": user.auth_token.key})
        else:
            return Response({"error": "Wrong Credentials"}, status=status.HTTP_400_BAD_REQUEST)