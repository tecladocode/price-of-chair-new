from functools import wraps
from typing import Callable
from flask import session, flash, redirect, url_for, request


def requires_login(f: Callable) -> Callable:
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not session.get('email'):
            flash(u'You need to be signed in for this page.')
            return redirect(url_for('users.login_user', next=request.path))
        return f(*args, **kwargs)

    return decorated_function
