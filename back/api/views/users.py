from flask import Blueprint
from flask_restful import Api
# from api.utilities.errors import errors
from back.api.resources.users import CreateUser, Login
from back.api.utils.errors import errors


users_bp = Blueprint('users_bp', __name__)
api = Api(users_bp, errors=errors)


api.add_resource(CreateUser, '/')
api.add_resource(Login, '/login')
