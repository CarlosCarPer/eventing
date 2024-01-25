from django.http import HttpResponse
from rest_framework.generics import ListCreateAPIView, RetrieveDestroyAPIView
from .serializers import EventsSerializer
from .models import Events

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

class EventsList(ListCreateAPIView):
    queryset = Events.objects.all()
    serializer_class = EventsSerializer

class EventsDetail(RetrieveDestroyAPIView):
    queryset = Events.objects.all()
    serializer_class = EventsSerializer
