from flask_restful import Resource, reqparse
from back.api.modals.movie import Movie
from back.api.schemas.movie import MovieSchema
from back.api.services.movies import MovieService
from flask_jwt_extended import jwt_required, get_jwt_identity




# Adding arguments to create user resource
save_movie_parser = reqparse.RequestParser()
save_movie_parser.add_argument('id', help='Movie id is required!', required=True)
save_movie_parser.add_argument('title', help='Email is required', required=True)
save_movie_parser.add_argument('overview', help='Password is required', required=True)
save_movie_parser.add_argument('adult', help='Password is required', required=True)
save_movie_parser.add_argument('poster_path', help='Password is required', required=True)
save_movie_parser.add_argument('backdrop_path', help='Password is required', required=True)
save_movie_parser.add_argument('popularity', help='Password is required', required=True)
save_movie_parser.add_argument('original_language', help='Password is required', required=True)
save_movie_parser.add_argument('genre_ids', help='Password is required', required=True)


movie_schema = MovieSchema()
movies_schema = MovieSchema(many=True)

class Movies(Resource):
    """

    """
    def get(self):
        # Get 100 movies from The Movie Database API
        # movies_from_api = fetch_all_movies_from_api()
        # genres = fetch_all_genres_from_api()
        # print(genres)
        # movies = [Movie.initialize_movie_from_json(movie, genres) for movie in movies_from_api]
        # for movie in movies:
        #     movie.save_movie_in_database()
        movies = MovieService.get_all()
        serialized_movies = movies_schema.dump(movies)
        return serialized_movies

    # adding movie to favorites
    def post(self):
        movie_details = save_movie_parser.parse_args()
        print(movie_details)
        res = MovieService.add_to_favorites(movie_details.id)
        return res


class FavoriteMovies(Resource):
    method_decorators = [jwt_required()]
    def get(self):
        user_id = get_jwt_identity()
        favorite_movies = MovieService.get_all_favorite_movies(user_id)
        return movies_schema.dump(favorite_movies)


class FavoriteMovie(Resource):
    method_decorators = [jwt_required()]
    def post(self, id: int):
        user_id = get_jwt_identity()
        res = MovieService.add_to_favorites(user_id, id)
        return res

    def delete(self, id: int):
        user_id = get_jwt_identity()
        res = MovieService.remove_from_favorites(user_id, id)
        return res
