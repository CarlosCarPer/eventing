from django.http import HttpResponse
from django.core.mail import EmailMessage
from django.contrib.auth import authenticate
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from rest_framework import status
from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UsersSerializer
from .tokens import account_activation_token
from .models import Users

class UsersCreate(CreateAPIView):
    authentication_classes = ()
    permission_classes = ()
    serializer_class = UsersSerializer

    def post(self, request):
        serializer = UsersSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return signinconfirm(user, request)
        return Response(serializer.errors)

class UsersDetail(RetrieveUpdateDestroyAPIView):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer

    def update(self, request, pk):
        if request.user.pk != pk:
            return Response('You are not allowed to update other user profile',403)
        return super().delete(request, pk)

    def delete(self, request, pk):
        if request.user.pk != pk:
            return Response('You are not allowed to delete other user account',403)
        return super().delete(request, pk)

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

def signinconfirm(user: Users, request):
    current_site = get_current_site(request)
    mail_subject = 'Activate your Eventing account.'
    message = render_to_string('acc_active_email.html', {
        'user': user.username,
        'domain': current_site.domain,
        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
        'token': account_activation_token.make_token(user),
    })
    email = EmailMessage(
                mail_subject, message, to=[user.email]
    )
    email.send()
    return Response('Please, check your inbox')

def activate(_, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = Users.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, Users.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        return HttpResponse('Thank you for your email confirmation. Now you can login your account.')
    else:
        return HttpResponse('Activation link is invalid!')