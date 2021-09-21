from flask import Blueprint
from flask_restful import Api
# from api.utilities.errors import errors
from back.api.resources.movies import Movies, FavoriteMovies, FavoriteMovie

movies_bp = Blueprint('movies_bp', __name__)
api = Api(movies_bp)


api.add_resource(Movies, '/')
api.add_resource(FavoriteMovies, '/favorites/')
api.add_resource(FavoriteMovie, '/favorites/<int:id>')

