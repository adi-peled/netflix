from marshmallow import Schema, fields
from back.api.modals.movie import Movie

class MovieSchema(Schema):
    class Meta:
        model = Movie
        ordered = True

    movie_id = fields.Integer(required=True)
    title = fields.String(required=True)
    description = fields.String(required=True)
    isAdult = fields.Boolean(required=True)
    poster = fields.String(required=True)
    background_image = fields.String(required=True)
    vote_average = fields.Float(required=True)
    vote_count = fields.Integer(required=True)
    language = fields.String(required=True)
    genre_list = fields.List(fields.String,required=True)