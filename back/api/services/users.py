from back.api.modals.user import User
from back.api.utils.database import save_changes
from flask import jsonify, make_response
from back.api.utils.errors import IncorrectPasswordError, IncorrectUsernameError, UsernameAlreadyExistsError
from flask_jwt_extended import create_access_token


class UserService:

    @classmethod
    def create_user(cls, data):
        user = cls.get_user(data['username'])
        if not user:
            new_user = User(username=data['username'], email=data['email'], password=data['password'])
            save_changes(new_user)
            response_object = {
                'status_code': 201,
                'message': 'Successfully registered!'
            }
            return make_response(jsonify(response_object['message']), response_object['status_code'])
        else:
            raise UsernameAlreadyExistsError

    @classmethod
    def login(cls, data):
        username = data.get('username')
        password = data.get('password')
        user = cls.get_user(username)
        if user is None:
            raise IncorrectUsernameError

        if not user.verify_password(password):
            raise IncorrectPasswordError

        else:
            token = create_access_token(identity=user.get_id())
            response_object = {
                'Status_code': 200,
                'Message': {'Access Token': token}
            }
            return make_response(jsonify(response_object['Message']), response_object['Status_code'])

    @staticmethod
    def get_user(username):
        return User.query.filter_by(username=username).first()


