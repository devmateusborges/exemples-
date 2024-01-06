from json import loads
import json
import os
import shutil
from unittest import TestCase
from app.utils.redis_util import redis_util
from generic_ids import fixed_ids
from app import create_app
from flask import url_for


# ====================================================================================================
class generic_tests(TestCase):

    # ====================
    def setUp(self):

        dir_test = os.path.dirname(__file__)
        dir_test = dir_test + os.sep + "downloads"
        # os.removedirs(dir_test)

        for file_object in os.listdir(dir_test):
            file_object_path = os.path.join(dir_test, file_object)
            if os.path.isfile(file_object_path) or os.path.islink(file_object_path):
                os.unlink(file_object_path)
            else:
                shutil.rmtree(file_object_path)

        self.app = create_app()
        self.app.testing = True
        self.app_context = self.app.test_request_context()
        self.app_context.push()
        self.client = self.app.test_client()
        # TODO Ajustar depois com migrations
        # self.app.db.create_all()
        self.login = {
            "login": "admin",
            "password": "123",
            "unit_id": "f3996813-838e-49af-9649-8dc44e24bc75",
        }
        self.session = redis_util.get_conn_cache()

    # ====================
    def tearDown(self):
        pass
        # TODO Cuidado so deve ser executado com banco nome **_test
        # self.app.db.drop_all()

    # ====================
    def create_user(self):
        self.client.post(url_for("auth.register"), json=self.user)

    # ====================
    def create_token(self):
        token = self.session.get("access_token")
        if token is None:
            login = self.client.post(url_for("auth.login"), json=self.login)
            token = loads(login.data.decode())["access_token"]
            self.session.set("access_token", token)
        else:
            token = token.decode()

        return {"Authorization": "Bearer " + token}

    # ====================
    def check_scenary(self, A, B):
        n = -1
        while True:
            try:
                n = A.index(B[0], n + 1)
            except ValueError:
                return False
            if A[n : n + len(B)] == B:
                return True

    # ====================
    def get_id_fixed(self, column):
        return fixed_ids[column]

    # ====================
    def session_flushdb(self):
        self.session.flushdb()

    # ====================
    def get_id_response(self, response):
        try:
            id = json.loads(response.data.decode())["id"]
            return id
        except:
            print(">>>>> get_id_response ====================================")
            print(response)
            print(">>>>> get_id_response>data ====================================")
            print(response.data)
