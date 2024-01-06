import datetime
import logging
import sys

import sentry_sdk
from flask import Flask, jsonify
from flask_jwt_extended import JWTManager
from flask_migrate import Migrate
from flask_cors import CORS
from sentry_sdk.integrations.flask import FlaskIntegration
import rq_dashboard

from app.env import (
    DB_DATABASE,
    DB_HOST,
    DB_PASSWORD,
    DB_PORT,
    DB_USERNAME,
    DEBUG,
    DEBUG_QUERY,
    LOG_SENTRY_URL,
    SECRET_KEY,
    STORAGE_UPLOAD_FOLDER,
    VERSION_BUILD,
    RQ_DASHBOARD_USERNAME,
    RQ_DASHBOARD_PASSWORD,
    RQ_DASHBOARD_REDIS_URL,
)

from .configs.config_db import configure as config_db
from .configs.config_routes import configure as config_routes
from .configs.config_serealizer import configure as config_serealizer
from .configs.config_session import configure as config_session
from .configs.config_auth_social import configure as config_auth_social
from .configs.config_template import configure as config_template
from .configs.config_cli import configure as config_cli
from .configs.config_cache import configure as config_cache
from .configs.config_errorhandler import configure as config_errorhandler


logging.basicConfig(
    filename="./app.log",
    format="%(asctime)s %(filename)s: %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
handler = logging.StreamHandler(sys.stdout)
handler.setLevel(logging.DEBUG)
handler.setFormatter(
    logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
)
logger.addHandler(handler)


# ===============================
app = Flask(
    __name__,
    static_url_path="/static",
    static_folder="static",
    template_folder="templates",
)
# ===============================


app.config["RQ_DASHBOARD_REDIS_URL"] = RQ_DASHBOARD_REDIS_URL
app.config["RQ_DASHBOARD_USERNAME"] = RQ_DASHBOARD_USERNAME
app.config["RQ_DASHBOARD_PASSWORD"] = RQ_DASHBOARD_PASSWORD
app.register_blueprint(rq_dashboard.blueprint, url_prefix="/api/rq")
# ===============================
sentry_sdk.init(
    dsn=LOG_SENTRY_URL,
    integrations=[
        FlaskIntegration(),
    ],
    traces_sample_rate=1.0,
    _experiments={
        "profiles_sample_rate": 1.0,
    },
)

# ===============================
cors = CORS(app, resources={r"/*": {"origins": "*"}})

# ==============================
app.config["SECRET_KEY"] = SECRET_KEY
url_db = (
    f"""postgresql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_DATABASE}"""
)
app.config["SQLALCHEMY_DATABASE_URI"] = url_db
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_POOL_SIZE"] = 20
app.config["SQLALCHEMY_DISABLE_POOL"] = False
app.config["SQLALCHEMY_MAX_OVERFLOW"] = 0
app.config["SQLALCHEMY_ECHO"] = DEBUG_QUERY
app.config["JWT_SECRET_KEY"] = SECRET_KEY
app.config["UPLOAD_FOLDER"] = STORAGE_UPLOAD_FOLDER
app.config["PERMANENT_SESSION_LIFETIME"] = datetime.timedelta(minutes=5)

# ==============================
config_session(app)


# ==============================
db = config_db(app)
Migrate(app=app, db=db, directory="migrations", version_table="sys_migration")

# ==============================
ma = config_serealizer(app)

# ==============================
jwt = JWTManager(app)


# ==============================
config_auth_social(app)

# ==============================
config_cli(app)

# ==============================
cache = config_cache(app)


@jwt.user_lookup_loader
def user_lookup_callback(_jwt_header, jwt_data):
    from app.modules.sys.base.sys_model import SysUnit, SysUser

    user_id = jwt_data["sub"]
    unit_id = jwt_data["unit_id"]
    user = SysUser.query.filter_by(id=user_id).one_or_none()
    unit = SysUnit.query.filter_by(id=unit_id).one_or_none()
    result = []
    result.append(user)
    result.append(unit)
    return result


# ==============================
tpl = config_template(app)

# ==============================


@app.route("/", methods=["GET"])
def route_init():
    return (
        jsonify(
            {
                "datetime": datetime.datetime.now().strftime("%d/%m/%YT%H:%M:%S.%f"),
                "code": "200",
                "name": "HEALTH_CHECK",
                "msg": f"The server is running BUILD_VERSION: {VERSION_BUILD}",
            }
        ),
        200,
    )


@app.route("/debug-sentry")
def trigger_error():
    division_by_zero = 1 / 0


# ==============================
config_routes(app)


def create_app(app=app):
    return app


# ===============================
if __name__ == "__main__":
    app.run(debug=(DEBUG == 1))

# ===============================


# ===============================
@app.teardown_appcontext
def shutdown_session(response_or_exc):
    print(">>>teardown_appcontext")

    # TODO executado ao final de todas subida e baixa contexto da aplicacao

    return response_or_exc


# ===============================


@app.errorhandler(Exception)
def errorhandler(e):
    return config_errorhandler(e)
