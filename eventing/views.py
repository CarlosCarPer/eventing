from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.permissions import BasePermission

from .serializers import EventsSerializer
from .models import Events

def index(request):
    return Response("Hello, world. You're at the polls index.")

class IsAuthenticatedAndMember(BasePermission):
    message = 'You must be a member of this event.'

    def has_permission(self, request, _):
        return request.user and request.user.is_authenticated

    def has_object_permission(self, request, _, obj):
        return request.user in obj.members.all()

class EventsList(ListCreateAPIView):
    serializer_class = EventsSerializer

    def get_queryset(self):
        return self.request.user.events.all()

    def perform_create(self, serializer: EventsSerializer):
        author = self.request.user
        members = set(serializer.validated_data['members'])
        members.add(author)
        serializer.save(author=author,members=members)

class EventsDetail(RetrieveUpdateDestroyAPIView):
    queryset = Events.objects.all()
    serializer_class = EventsSerializer
    permission_classes = (IsAuthenticatedAndMember,)

@api_view(['GET'])
def add_member(request, pk, mpk):
    event = Events.objects.get(pk=pk)
    if request.user.pk == event.author.pk:
        event.members.add(mpk)
        event.save()
        return Response()
    return Response()

@api_view(['GET'])
def remove_members(request, pk, mpk):
    event = Events.objects.get(pk=pk)
    if request.user.pk == event.author.pk:
        event.members.remove(mpk)
        event.save()
        return Response()
    return Response()