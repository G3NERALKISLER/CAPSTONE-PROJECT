from django.urls import path
from . import views
urlpatterns = [
    path('', views.movie_list, name='movies'),
    path('<str:imdb_id>/', views.movie_detail, name='movie_detail'),

]