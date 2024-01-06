from flask_session import Session
from app.env import SESSION_TYPE
from app.utils.redis_util import redis_util

msession = Session()

# ======


def configure(app):
    print(">>>Init SESSION")
    app.config["SESSION_TYPE"] = SESSION_TYPE
    app.config["SESSION_REDIS"] = redis_util.get_conn_cache()
    msession.init_app(app)
    app.session = msession
    return msession
