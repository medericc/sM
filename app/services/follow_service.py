from app.models.follow import Follow
from app import db

def follow_user(follower_id, followed_id):
    follow = Follow(following_user_id=follower_id, followed_user_id=followed_id)
    db.session.add(follow)
    db.session.commit()
    return follow
