import requests
from django.shortcuts import render
from .models import Movie
# Create your views here.
def movie_list(request):
   api_key = '5891d27a'  # replace this with your OMDb key
   query = 'marvel'  # or any keyword you like
   url = f'https://www.omdbapi.com/?apikey={api_key}&s={query}'

   response = requests.get(url)
   data = response.json()

    # check if response contains movies
   movies = data.get('Search', [])
   local_movies = Movie.objects.all()
   all_movies = list(local_movies) + movies
   return render(request, 'movies/movie_list.html', {'movies': all_movies})

def movie_detail(request, imdb_id):
   api_key = '5891d27a'
   url = f'https://www.omdbapi.com/?apikey={api_key}&i={imdb_id}&plot=full'
   response = requests.get(url)
   data = response.json()
   return render(request, 'movies/movie_detail.html', {'movie': data})