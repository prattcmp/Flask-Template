from flask_sqlalchemy import SQLAlchemy
from ..Models import db


# Creating the post table
class Post(db.Model):
    __tablename__ = 'posts'
    # Creating the columns of the posts table
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    content = db.Column(db.String(280))
    comments = db.relationship('Comment', backref='post', lazy=True)
    ip_address = db.Column(db.String(50))
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    modified_at = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())

    def __init__(self, content, user_id, ip_address):
        self.content = content
        self.user_id = user_id
        self.ip_address = ip_address


class Comment(db.Model):
    __tablename__ = 'comments'
    # Creating the columns of the comments table
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    post_id = db.Column(db.Integer, db.ForeignKey('posts.id'), nullable=False)
    content = db.Column(db.String(280))
    ip_address = db.Column(db.String(50))
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    modified_at = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())

    def __init__(self, content, post_id, user_id, ip_address):
        self.content = content
        self.post_id = post_id
        self.user_id = user_id
        self.ip_address = ip_address
