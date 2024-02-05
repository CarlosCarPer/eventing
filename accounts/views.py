from django.core.mail import send_mail
from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UsersSerializer

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

def signinconfirm():
    send_mail(
        "Eventing",
        "Confirma tu cuenta clickando en el siguinte enlace:.",
        "carlos.carraper@gmail.com",
        ["carcisco97@gmail.com"],
        fail_silently=False,
        )