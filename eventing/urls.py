from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("events/", views.EventsList.as_view(), name="events_list"),
    path("events/<int:pk>/", views.EventsDetail.as_view(), name="events_detail")
]