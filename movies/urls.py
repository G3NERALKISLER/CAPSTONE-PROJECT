from django.urls import path
from . import views
from .views import MovieListAPIView, MovieDetailAPIView
app_name = 'movies'
urlpatterns = [
    path('', views.movie_list, name='movies'),
    path('<str:imdb_id>/', views.movie_detail, name='movie_detail'),
    path('api/movies/', MovieListAPIView.as_view(), name='api-movie-list'),
    path('api/movies/<int:pk>/', MovieDetailAPIView.as_view(), name='api-movie-detail'),

]
