from rest_framework.generics import ListAPIView

from .models import Movie, Banner, Genre, Actor
from .serializer import AllMoviesSerializer, BannerSerializer, ActorSerializer, GenreSerializer


# Create your views here.

class AllMoviesView(ListAPIView):
    serializer_class = AllMoviesSerializer
    queryset = Movie.objects.all().order_by('id')
    filterset_fields = ['original_name', 'persian_name']


class BannerView(ListAPIView):
    serializer_class = BannerSerializer
    queryset = Banner.objects.all().order_by('id')


class GenreView(ListAPIView):
    serializer_class = GenreSerializer
    queryset = Genre.objects.all().order_by('id')


class ActorView(ListAPIView):
    serializer_class = ActorSerializer
    queryset = Actor.objects.all().order_by('id')
