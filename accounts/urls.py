from django.urls import path
from . import views

urlpatterns = [
    path("register/", views.UsersCreate.as_view(), name="register"),
    path('activate/<uidb64>/<token>', views.activate, name='activate'),
    path("users/<int:pk>/", views.UsersDetail.as_view(), name="user_detail"),
    path("login/", views.LoginView.as_view(), name="login")
]