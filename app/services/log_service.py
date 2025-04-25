from ..models import Log
from .. import db

def log_action(user_id, action, target_type, target_id, details=None):
    log = Log(
        user_id=user_id,
        action=action,
        target_type=target_type,
        target_id=target_id,
        details=details
    )
    db.session.add(log)
    db.session.commit()
