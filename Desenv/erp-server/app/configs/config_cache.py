from flask_caching import Cache

from app.env import CACHE_TIMEOUT, SESSION_DB, SESSION_HOST, SESSION_PORT, SESSION_PWD


# ======


def configure(app):
    print(">>>Init CACHE")
    app.config["CACHE_TYPE"] = "RedisCache"
    app.config["CACHE_DEFAULT_TIMEOUT"] = CACHE_TIMEOUT
    app.config["CACHE_REDIS_HOST"] = SESSION_HOST
    app.config["CACHE_REDIS_PORT"] = SESSION_PORT
    app.config["CACHE_REDIS_PASSWORD"] = SESSION_PWD
    app.config["CACHE_REDIS_DB"] = SESSION_DB
    cache = Cache()
    cache.init_app(app)
    app.cache = cache
    return cache
