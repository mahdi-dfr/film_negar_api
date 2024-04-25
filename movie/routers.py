from django.urls import path
from rest_framework.routers import DefaultRouter

from movie.views import AllMoviesView, BannerView, GenreView, ActorView

router = DefaultRouter()
# router.register('movie', AllMoviesView, basename='movie'),
urlpatterns = [
                  path('movie/', AllMoviesView.as_view(), name='movie'),
                  path('banner/', BannerView.as_view(), name='movie'),
                  path('genre/', GenreView.as_view(), name='movie'),
                  path('actor/', ActorView.as_view(), name='movie'),
              ] + router.urls
