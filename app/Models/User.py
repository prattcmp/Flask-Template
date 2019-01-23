from flask_sqlalchemy import SQLAlchemy
from ..Models import db


# Creating the user table
class User(db.Model):
    __tablename__ = 'users'
    # Creating the columns of the user table
    id = db.Column(db.Integer, primary_key=True)
    secret_key = db.Column(db.String(128))
    posts = db.relationship('Post', backref='user', lazy=True)
    comments = db.relationship('Comment', backref='user', lazy=True)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    modified_at = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())

    def __init__(self, id=None, secret_key=None):
        if id is not None:
            self.id = id
            
        if secret_key is not None:
            self.secret_key = secret_key
