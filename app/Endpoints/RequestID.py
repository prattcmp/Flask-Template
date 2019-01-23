from flask import Blueprint, request, jsonify
from ..Models import db

import binascii
import os

request_id = Blueprint('request_id', __name__)
       
from ..Models.User import User


def generateSecretKey(length):
    return binascii.hexlify(os.urandom(length // 2)).decode()


# endpoint to request a new ID
@request_id.route("/request_id", methods=["POST"])
def request_user_id():
    data = request.get_json()

    new_user = User(secret_key=generateSecretKey(128))

    db.session.add(new_user)
    db.session.commit()

    json = {
        "user_id": new_user.id,
        "user_secret_key": new_user.secret_key
    }
    return jsonify(json), 200
