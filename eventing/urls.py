from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("events/", views.EventsList.as_view(), name="events_list"),
    path("events/<int:pk>/", views.EventsDetail.as_view(), name="events_detail"),
    path("events/<int:pk>/add_members/<int:mpk>/", views.add_member, name='add_member'),
    path("events/<int:pk>/remove_members/<int:mpk>/", views.remove_members, name='remove_members'),
    path("events/<int:pk>/tasks/", views.EventsTasks.as_view(), name='tasks'),
    path("tasks/<int:pk>/", views.TaskDetail.as_view(), name='tasks_detail')
]