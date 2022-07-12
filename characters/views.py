from rest_framework.viewsets import ModelViewSet
from .models import Character, Location, Episode
from .serializer import CharacterSerializer, LocationSerializer, EpisodeSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser

class CharacterViewSet(ModelViewSet):
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer
    permission_classes = [IsAuthenticatedOrReadOnly | IsAdminUser]

class LocationViewSet(ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
    permission_classes = [IsAuthenticatedOrReadOnly | IsAdminUser]

class EpisodeViewSet(ModelViewSet):
    queryset = Episode.objects.all()
    serializer_class = EpisodeSerializer
    permission_classes = [IsAuthenticatedOrReadOnly | IsAdminUser]