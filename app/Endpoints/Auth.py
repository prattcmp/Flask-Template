from functools import wraps
from flask import Blueprint, request, jsonify

from ..Models import db
from ..Models.User import User

auth = Blueprint('auth', __name__)


# Verify that the user secret key is valid
def user_secret_required(func):
    @wraps(func)
    def decorated_function(*args, **kwargs):
        if request.method == 'POST':
            data = request.get_json()
        else:
            data = request.args

        user_id = data.get('user_id')
        user_secret_key = data.get('user_secret_key')

        user = User.query.filter_by(id=user_id, secret_key=user_secret_key).first()
        if user is None:
            error = "You are unauthorized to make this request."
            return jsonify({'error': error}), 401

        request.user = user

        return func(*args, **kwargs)
    return decorated_function


@auth.route("/verify_account", methods=["POST"])
@user_secret_required
def verify_account():
    user = request.user

    json = {
        "user_id": user.id
    }

    return jsonify(json), 200


@auth.route("/health_check", methods=["get"])
def health_check():

    json = {
        "health": "OK"
    }

    return jsonify(json), 200
