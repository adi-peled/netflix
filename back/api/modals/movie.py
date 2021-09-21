from back.api import db
from back.api.modals.user import User

class FavoriteMovie(db.Model):
    """
        Favorite Movie Model for storing the movies users likes
    """
    __tablename__ = "Favorite_Movies"
    _id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('Users._id'), nullable=False)
    movie_id = db.Column(db.Integer, db.ForeignKey('Movies.movie_id'), nullable=False)

    def __init__(self, user_id: int, movie_id: int):
        self.user_id = user_id
        self.movie_id = movie_id


class Movie(db.Model):
    """
        Movie Model for storing Movie related details
    """
    __tablename__ = "Movies"
    __table_args__ = {'extend_existing': True}
    _id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    movie_id = db.Column(db.Integer, unique=True, nullable=False)
    title = db.Column(db.String(128), nullable=False)
    description = db.Column(db.String(1000), nullable=False)
    isAdult = db.Column(db.Boolean, nullable=False)
    poster = db.Column(db.String(128), nullable=False)
    background_image = db.Column(db.String(128), nullable=False)
    vote_average = db.Column(db.Float, nullable=False)
    vote_count = db.Column(db.Integer, nullable=False)
    language = db.Column(db.String(64), nullable=False)
    genre_list = db.Column(db.ARRAY(db.String(64)), nullable=True)

    def __init__(self, id: int, title: str, description: str,
                       adult: bool, poster: str, background_image: str,
                       vote_average: float, vote_count: int, language: str, genre_list: list = None) -> None:

        self.movie_id = id
        self.title = title
        self.description = description
        self.isAdult = adult
        self.poster = poster
        self.background_image = background_image
        self.vote_average = vote_average
        self.vote_count = vote_count
        self.language = language
        self.genre_list = genre_list

    @classmethod
    def initialize_movie_from_json(cls, movie_details, genres):
        movie_object = cls(movie_details['id'], movie_details['title'], movie_details['overview'],
                             movie_details['adult'], movie_details['poster_path'], movie_details['backdrop_path'],
                             movie_details['vote_average'], movie_details['vote_count'], movie_details['original_language'])
        # print(movie_object)
        movie_object.genre_list = [genre['name'] for genre in genres if genre['id'] in movie_details['genre_ids']]
        return movie_object

    @classmethod
    def get_all_movies(cls):
        movie_list = cls.query.all()
        return movie_list


    def watch_movie(self, movie_details):
        pass


    def save_movie_in_database(self):
        movie_object = Movie.query.filter_by(movie_id=self.movie_id).first()
        if movie_object is None:
            db.session.add(self)
            db.session.commit()


    def __repr__(self):
        return "<Movie '{}'>".format(self.title)