from functools import wraps

from flask import current_app, request

from app.utils.funcs_util import funcs_util

# ==============================


def unit_required():
    def wrapper(fn):
        @wraps(fn)
        def decorator(*args, **kwargs):
            unitid = request.headers.get("x-unitid")
            if unitid is None:
                funcs_util.ExceptionRequiredValue(unitid, "Unit")
            return current_app.ensure_sync(fn)(*args, **kwargs)

        return decorator

    return wrapper
