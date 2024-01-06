import redis

from app.env import (
    SESSION_DB,
    SESSION_HOST,
    SESSION_PORT,
    SESSION_PWD,
    RQ_DASHBOARD_REDIS_URL,
)


class redis_util:

    # ============================================================
    @staticmethod
    def get_conn_cache():
        return redis.StrictRedis(
            host=SESSION_HOST, port=SESSION_PORT, password=SESSION_PWD, db=SESSION_DB
        )

    # ============================================================
    @staticmethod
    def get_conn_queue():
        return redis.from_url(url=RQ_DASHBOARD_REDIS_URL)
