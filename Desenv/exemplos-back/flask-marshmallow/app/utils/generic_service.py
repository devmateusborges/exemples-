from flask import current_app
from typing import Any
from flask_jwt_extended import current_user
from sqlalchemy import delete

from app.exceptions.ApiException import ApiException

class generic_service():
    model: Any
     
    def __init__(self,model):
        self.model = model
    
    #==============================
    def find_all(self):
        if current_user is not None:
            print(">>>",current_user[0].login)
            print(">>>",current_user[1].sigla_unit)
        
        objs = current_app.db.session.query(self.model).all()
        
        return objs

    #==============================
    def find_by_id(self,id):
        obj = current_app.db.session.query(self.model).filter(self.model.id == id).first()
        
        return obj

    #==============================
    def save(self,obj):
        current_app.db.session.add(obj)
        
        return obj        

    #==============================
    def delete(self,id):
        obj = current_app.db.session.query(self.model).filter(self.model.id==id).first()
        if (obj is None):
            raise ApiException("Record id["+id+"] not found", status_code=400)

        current_app.db.session.query(self.model).filter(self.model.id==id).delete()
        
        return "deleted"        