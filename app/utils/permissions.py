from ..models import User

def check_permissions(current_user_id, owner_id, allow_subadmin=False):
    if current_user_id == owner_id:
        return True
    user = User.query.get(current_user_id)
    if user.role == 'admin':
        return True
    if allow_subadmin and user.role == 'subadmin':
        return True
    return False
