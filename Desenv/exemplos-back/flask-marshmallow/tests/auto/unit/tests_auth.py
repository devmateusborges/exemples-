import uuid

from flask import url_for
from tests.auto.generic_tests import generic_tests


class tests_user(generic_tests):
    """ def test_auth_user_register(self):
        
        uuidUser = uuid.uuid4()

        req_post = {   
                "name":"admin"+str(uuidUser),
                "login":"admin"+str(uuidUser),
                "password":"123",
                "email":"admin"+str(uuidUser)+"@admin.com"
            }

        response = self.client.post(url_for('auth.register'), json=req_post)
        
        self.assertEqual(response.status_code, 201) """


