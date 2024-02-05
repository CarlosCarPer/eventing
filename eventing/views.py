from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework.exceptions import PermissionDenied
from .serializers import EventsSerializer
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