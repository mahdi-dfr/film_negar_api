from rest_framework.serializers import ModelSerializer
from .models import Movie, Actor, Genre, Banner
from rest_framework import serializers


class AllMoviesSerializer(ModelSerializer):
    class Meta:
        model = Movie
        fields = "__all__"


class ActorSerializer(ModelSerializer):
    image = serializers.CharField(max_length=2000, required=False)

    class Meta:
        model = Actor
        fields = "__all__"


class GenreSerializer(ModelSerializer):
    class Meta:
        model = Genre
        fields = "__all__"


class BannerSerializer(ModelSerializer):
    class Meta:
        model = Banner
        fields = "__all__"
        depth = 2


