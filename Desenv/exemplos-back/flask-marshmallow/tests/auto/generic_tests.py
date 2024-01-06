from json import loads
import os
import shutil
from unittest import TestCase

import redis
from app import create_app
from flask import url_for

from app.env import SESSION_DB, SESSION_HOST, SESSION_PORT, SESSION_PWD


class generic_tests(TestCase):
    def setUp(self):
        """Roda antes de todos os testes."""
        
        dir_test = os.path.dirname(__file__) 
        dir_test = dir_test+os.sep+'unit'+os.sep+'downloads'
        #os.removedirs(dir_test)
        
        
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
        #TODO Ajustar depois com migrations
        #self.app.db.create_all()
        self.login = {   
            "login":"admin1",
            "password":"123",
            "unit_id":"f3996813-838e-49af-9649-8dc44e24bc75"
            }
        self.session = redis.StrictRedis(host=SESSION_HOST,port=SESSION_PORT,password=SESSION_PWD,db=SESSION_DB)    

    def tearDown(self):
        pass
        #TODO Cuidado so deve ser executado com banco nome **_test
        #self.app.db.drop_all()

    def create_user(self):
        self.client.post(url_for('auth.register'), json=self.user)

    def create_token(self):
        login = self.client.post(url_for('auth.login'), json=self.login)
        return {
            'Authorization':
                'Bearer ' + loads(login.data.decode())['acess_token']
        }
     
  