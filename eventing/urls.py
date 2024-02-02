from django.urls import path
from . import views
from .views import EventsList, EventsDetail, LoginView, UsersCreate

urlpatterns = [
    path("", views.index, name="index"),
    path("events/", EventsList.as_view(), name="events_list"),
    path("events/<int:pk>/", EventsDetail.as_view(), name="events_detail"),
    path("users/", UsersCreate.as_view(), name="user_create"),
    path("login/", LoginView.as_view(), name="login")
]