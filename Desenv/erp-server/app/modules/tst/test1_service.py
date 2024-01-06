import time

from app.generics.generic_service import generic_service
from rq import Queue, Connection
from app.utils.funcs_util import funcs_util

from app.utils.redis_util import redis_util

# ==============================
def test1_test_task(param):
    time.sleep(10)
    funcs_util.print(
        "test1_test_task", f"test1_test_task call queue executed param[{param}]"
    )


# ==============================
class test1_service(generic_service):

    # ==============================
    def test1_create_task(self, param):
        with Connection(redis_util.get_conn_queue()):
            q = Queue()
            task = q.enqueue(test1_test_task, param)
            result = {
                "code": "200",
                "data": {"task_id": task.get_id()},
                "name": "SUCCESS",
                "msg": "Successfully created",
            }
        return result
