from rest_framework.decorators import action
from rest_framework.generics import ListAPIView
from rest_framework.viewsets import ModelViewSet

from .models import Movie, Banner, Genre, Actor
from .serializer import AllMoviesSerializer, BannerSerializer, ActorSerializer, GenreSerializer


# Create your views here.

class AllMoviesView(ModelViewSet):
    serializer_class = AllMoviesSerializer
    queryset = Movie.objects.all().order_by('id')
    filterset_fields = ['original_name', 'persian_name']


    def get_queryset(self):
        genre = self.request.query_params.get('genre')
        if genre:
            genre_id = Genre.objects.get(name=genre)
            return Movie.objects.filter(genre=genre_id)

        return super().get_queryset()


class BannerView(ModelViewSet):
    serializer_class = BannerSerializer
    queryset = Banner.objects.all().order_by('id')


class GenreView(ModelViewSet):
    serializer_class = GenreSerializer
    queryset = Genre.objects.all().order_by('id')


class ActorView(ModelViewSet):
    serializer_class = ActorSerializer
    queryset = Actor.objects.all().order_by('id')
