from functools import wraps
from flask import jsonify
from flask_jwt_extended import get_jwt_identity
from .models import User

def admin_required(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        current_user_id = int(get_jwt_identity())
        user = User.query.get(current_user_id)
        if not user or not user.is_admin:
            return jsonify({'message':'Admins only'}),403
        return fn(*args,**kwargs)
    return wrapper
        