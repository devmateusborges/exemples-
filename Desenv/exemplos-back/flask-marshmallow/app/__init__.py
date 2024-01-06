import json
import logging

import sys
import traceback
from datetime import datetime
from http.client import HTTPException
from typing import Any

import redis



from app.exceptions.ApiException import ApiException
from app.modules.sys.base.sys_model import SysUnit, SysUser

logging.basicConfig(filename="./app.log", format='%(asctime)s %(filename)s: %(message)s',datefmt='%Y-%m-%d %H:%M:%S')
root = logging.getLogger()
root.setLevel(logging.DEBUG)
handler = logging.StreamHandler(sys.stdout)
handler.setLevel(logging.DEBUG)
handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
root.addHandler(handler)

from flask import Flask, Response, current_app, jsonify
from flask_jwt_extended import JWTManager
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from app.env import DB_URL, DEBUG, DEBUG_QUERY, SECRET_KEY, STORAGE_UPLOAD_FOLDER



#================================================================
app = Flask(__name__,
        static_url_path='/static', 
        static_folder='static',
        template_folder='templates')
        
# ===============================================================

app.config['SECRET_KEY'] = SECRET_KEY
app.config['SQLALCHEMY_DATABASE_URI'] = DB_URL
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_POOL_SIZE'] = 20
app.config['SQLALCHEMY_DISABLE_POOL'] = False
app.config['SQLALCHEMY_MAX_OVERFLOW'] = 0
app.config['SQLALCHEMY_ECHO'] = DEBUG_QUERY
app.config['JWT_SECRET_KEY'] = SECRET_KEY
app.config['UPLOAD_FOLDER'] = STORAGE_UPLOAD_FOLDER



# ===============================================================
from .configs.config_session import configure as config_session
msession = config_session(app)
app.session = msession
  

# ===============================================================
from .configs.config_model import configure as config_db
db = config_db(app)
app.db = db
Migrate(app=app, db=app.db,directory="migrations", version_table = "sys_migration")

# ===============================================================
from .configs.config_serealizer import configure as config_serealizer
config_serealizer(app)

# ===============================================================
jwt = JWTManager(app)
@jwt.user_lookup_loader
def user_lookup_callback(_jwt_header, jwt_data):
    user_id = jwt_data["sub"]
    unit_id = jwt_data["unit_id"]
    user = SysUser.query.filter_by(id=user_id).one_or_none()
    unit = SysUnit.query.filter_by(id=unit_id).one_or_none()
    result = []
    result.append(user)
    result.append(unit)
    return result

# ===============================================================
from .configs.config_template import configure as config_template
tpl = config_template(app)
app.tpl = tpl

# ===============================================================
from .configs.config_routes import configure as config_route
config_route(app)



#================================================================
if __name__ == "__main__":
     app.run(debug=DEBUG)

def create_app(app=app):
    return app


#================================================================
@app.teardown_appcontext
def shutdown_session(response_or_exc):
    print('>>>teardown_appcontext')
    #TODO executado ao final de todas request
    
    return response_or_exc

#================================================================
@app.errorhandler(Exception)
def configure(e):
    try:
        if isinstance(e, HTTPException):
            
            logging.error(e.name+' - '+e.description)    
            response = e.get_response()
            response.data = json.dumps({
                "datetime": datetime.now().strftime('%d/%m/%Y  %H:%M:%S.%f'),
                "code": e.code,
                "name": e.name,
                "msg": e.description,
            })
            response.content_type = "application/json"
            return response

        elif isinstance(e, ApiException):
            response = jsonify(e.to_dict())
            response.status_code = e.status_code
            return response

        
        else:
            logging.error('Internal Error - '+traceback.format_exc())    
            description = str(traceback.format_exc())
            description = description.replace('\n',' ')
            description = description.replace('  ',' ')
            #===============
            index1 = description.find('RuntimeError:')
            
            #===============
            if index1 < 0:
                index1 = description.find('ValueError:')
            
  
            descriptionStart = int(index1)
            descriptionEnd = int(len(description)-descriptionStart)
            description = description[-descriptionEnd:]
            
            #===============
            if index1 < 0:
                index1 = description.find('sqlalchemy.exc.IntegrityError:')
                if index1 > 0:
                    description = "Unique constraint violate"

            #===============
            if index1 < 0:
                index1 = description.find('duplicate key value violates unique constraint')
                if index1 > 0:
                    description = "Unique constraint violate"

            #===============
            if index1 < 0:
                index1 = description.find('Failed to decode JSON object')
                if index1 > 0:
                    description = "Json body invalid"
            
            #===============
            if index1 < 0:
                index1 = description.find('jinja2.exceptions.TemplateNotFound:')
                if index1 > 0:
                    description = "Template not found"                    
            
            response = Response()
            response.status_code = 500
            response.data = json.dumps({
                "datetime": datetime.now().strftime('%d/%m/%Y  %H:%M:%S.%f'),
                "code": 500,
                "name": 'Internal Error',
                "msg": description
            })
            response.content_type = "application/json"
            return response
    except Exception as e:
        response = Response()
        response.status_code = 500
        response.data = json.dumps({
                "datetime": datetime.now().strftime('%d/%m/%Y  %H:%M:%S.%f'),
                "code": 500,
                "name": 'Internal Error',
                "msg":str(traceback.format_exc())
            })
        response.content_type = "application/json"
        return response
  
  
    
      
