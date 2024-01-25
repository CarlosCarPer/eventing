from django.urls import path
from . import views
from .views import EventsList, EventsDetail

urlpatterns = [
    path("", views.index, name="index"),
    path("events/", EventsList.as_view(), name="events_list"),
    path("events/<int:pk>/", EventsDetail.as_view(), name="events_detail")
]