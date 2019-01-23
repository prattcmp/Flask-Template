from flask import Blueprint, request, jsonify
from sqlalchemy import and_, exists, func

from ..Models import db
from ..Endpoints.Auth import user_secret_required

posts = Blueprint('posts', __name__)

from ..Models.Post import Post, Comment


# endpoint to create a new post
@posts.route("/create_post", methods=["POST"])
@user_secret_required
def create_post_comment():
    data = request.get_json()
    type = data.get('type', 'post')
    content = data['content']
    user_id = data['user_id']

    # Verify length of the post
    if len(content) > 280:
        error = "Your content cannot be more than 280 characters."
        return jsonify({'error': error}), 422

    if type == "comment":
        post_id = data.get('post_id')
        new_post = Comment(content, post_id, user_id, request.access_route[-1])
    else:
        new_post = Post(content, user_id, request.access_route[-1])

    db.session.add(new_post)
    db.session.commit()

    json = {
        "post_id": new_post.id,
        "content": new_post.content,
        "created_at": str(new_post.created_at)
    }
            
    return jsonify(json), 200


# endpoint to get a single posts
@posts.route("/get_post", methods=["GET"])
@user_secret_required
def get_post():
    data = request.args
    type = data.get('type', 'post')
    post_id = data.get('post_id')

    if type == "comment":
        post = Comment.query.filter_by(id=post_id).first()
    else:
        post = Post.query.filter_by(id=post_id).first()
        
    if post is None:
        error = "That post doesn't exist."
        return jsonify({'error': error}), 404
    
    replies = 0
    if type == "post":
        replies = db.session.query(func.count(Comment.id)).select_from(Comment).filter_by(post_id=post.id).scalar()

    json = {
        "post_id": post.id,
        "content": post.content,
        "created_at": str(post.created_at)
    }

    if type == "comment":
        json["owned_by"] = post.post_id
    else:
        json["replies"] = replies

    return jsonify(json), 200
