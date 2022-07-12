from rest_framework import serializers
from .models import Character, Location, Episode

class CharacterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Character
        fields = ('id', 'img', 'name', 'status', 'desc', 'race', 'gender', 'loc', 'birth_loc')


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ('id', 'img', 'title', 'izmerenie', 'desc')

class EpisodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Episode
        fields = ('id', 'img', 'title', 'numb_episode', 'desc', 'characters')