from django.urls import path
from rest_framework.routers import DefaultRouter

from movie.views import AllMoviesView, BannerView, GenreView, ActorView

router = DefaultRouter()
router.register('movie', AllMoviesView, basename='movie'),
router.register('banner', BannerView, basename='banner'),
router.register('genre', GenreView, basename='genre'),
router.register('actor', ActorView, basename='actor'),
urlpatterns = [] + router.urls
