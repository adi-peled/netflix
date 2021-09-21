from back.api.modals.movie import Movie, FavoriteMovie
from back.api.utils.database import save_changes, delete_row
from flask import jsonify

class MovieService:

    @staticmethod
    def get_all() -> [Movie]:
        movies = Movie.query.all()
        return movies

    @staticmethod
    def get_all_favorite_movies(user_id: int) -> [Movie]:
        movie_id_list = [id[0] for id in FavoriteMovie.query.with_entities(FavoriteMovie.movie_id).filter_by(user_id=user_id).all()]
        print(movie_id_list)
        favorite_movies = Movie.query.filter(Movie.movie_id.in_(movie_id_list)).all()
        return favorite_movies

    @staticmethod
    def add_to_favorites(user_id: int, movie_id: int) -> str:
        movie_to_favorite = FavoriteMovie(user_id, movie_id)
        save_changes(movie_to_favorite)
        return jsonify({"message":"Movie added to favorites"})


    @staticmethod
    def remove_from_favorites(user_id: int, movie_id: int) -> str:
        movie_to_remove = FavoriteMovie.query.filter_by(user_id=user_id, movie_id=movie_id).first()
        delete_row(movie_to_remove)
        return jsonify({"message":"Movie deleted from favorites"})
    # @staticmethod
    # def add_movie(movie_details) -> str:
    #     new_movie = Movie(movie_details)