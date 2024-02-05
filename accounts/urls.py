from django.urls import path
from . import views

urlpatterns = [
    path("users/", views.UsersCreate.as_view(), name="user_create"),
    path("login/", views.LoginView.as_view(), name="login")
]