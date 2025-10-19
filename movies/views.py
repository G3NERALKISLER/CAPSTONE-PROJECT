import requests
from rest_framework import generics
from django.shortcuts import render
from .models import Movie
from urllib.parse import quote
from reviews.models import Review
from .serializers import MovieSerializer
# Create your views here.
#views for displaying templates
def movie_list(request):
   api_key = '5891d27a'  
   query = request.GET.get('q') 
   if query:
        url = f'https://www.omdbapi.com/?apikey={api_key}&s={query}'
   else:
        url = f'https://www.omdbapi.com/?apikey={api_key}&s=series'
    
   response = requests.get(url)
   data = response.json()
 
   movies = data.get('Search', [])
   local_movies = Movie.objects.all()
   all_movies = list(local_movies) + movies

        
   return render(request, 'movies/movie_list.html', {'movies': all_movies, 'query': query,})

def movie_detail(request, imdb_id):
   api_key = '5891d27a'
   youtube_api_key = 'AIzaSyC09PGYTDQvBEZFJqKPLyHDprD2NyKVf4k'
   url = f'https://www.omdbapi.com/?apikey={api_key}&i={imdb_id}&plot=full'
   response = requests.get(url)
   data = response.json()
   reviews = Review.objects.filter(imdb_id=imdb_id)

   movie_title = data.get('Title', '')
   if movie_title:
        youtube_search_url = (
            f'https://www.googleapis.com/youtube/v3/search'
            f'?part=snippet'
            f'&q={movie_title}+official+trailer'
            f'&type=video'
            f'&maxResults=3'
            f'&key={youtube_api_key}'
        )
        yt_response = requests.get(youtube_search_url)
        yt_data = yt_response.json()

        trailer_id = None
        if yt_data.get('items'):
            
            for item in yt_data['items']:
                title = item['snippet']['title'].lower()
                if 'trailer' in title:
                    trailer_id = item['id']['videoId']
                    break
            if not trailer_id:
                trailer_id = yt_data['items'][0]['id']['videoId']
        else:
            trailer_id = None
   else:
        trailer_id = None

   return render(request, 'movies/movie_detail.html', {'movie': data, 'trailer':trailer_id, 'reviews' : reviews})
 # views for displaying api views

class MovieListAPIView(generics.ListAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    

class MovieDetailAPIView(generics.RetrieveAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer