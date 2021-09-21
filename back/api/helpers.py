import requests
from back.config import Config

base_url = 'https://api.themoviedb.org/3/movie/'

def fetch_all_movies_from_api():
    movies = []
    print(Config.TMDB_API_KEY)
    tmdb_url = f'{base_url}popular?api_key={Config.TMDB_API_KEY}&language=en-US'
    for i in range(1, 6):
        url = f'{tmdb_url}&page={i}'
        res = requests.get(url).json()['results']
        for item in res:
            movies.append(item)
        # print(res)
    return movies

def fetch_all_genres_from_api():
    tmdb_url = f'https://api.themoviedb.org/3/genre/movie/list?api_key={Config.TMDB_API_KEY}&language=en-US'
    res = requests.get(tmdb_url).json()['genres']
    print(res)
    return res