from app.models.follow import Follow
from app.models.user import User
from app import db
from flask import jsonify

def follow_user(follower_id, followed_id):
    if follower_id == followed_id:
        return jsonify({'error': 'You cannot follow yourself.'}), 400

    existing = Follow.query.filter_by(
        following_user_id=follower_id,
        followed_user_id=followed_id
    ).first()
    if existing:
        return jsonify({'message': 'Already following'}), 200

    follow = Follow(following_user_id=follower_id, followed_user_id=followed_id)
    db.session.add(follow)
    db.session.commit()
    return jsonify({'message': 'Followed successfully'}), 201


def unfollow_user(follower_id, followed_id):
    follow = Follow.query.filter_by(
        following_user_id=follower_id,
        followed_user_id=followed_id
    ).first()

    if not follow:
        return jsonify({'error': 'Follow not found'}), 404

    db.session.delete(follow)
    db.session.commit()
    return jsonify({'message': 'Unfollowed successfully'})


def get_followers(user_id):
    followers = Follow.query.filter_by(followed_user_id=user_id).all()
    return jsonify([{
        'id': f.following_user.id,
        'username': f.following_user.username,
        'email': f.following_user.email
    } for f in followers])


def get_following(user_id):
    following = Follow.query.filter_by(following_user_id=user_id).all()
    return jsonify([{
        'id': f.followed_user.id,
        'username': f.followed_user.username,
        'email': f.followed_user.email
    } for f in following])
