from functools import wraps
from os import abort

from flask_login import current_user


def role_required(role):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            if current_user.role != role:
                abort(403)
            return f(*args, **kwargs)
        return decorated_function
    return decorator