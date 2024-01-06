from flask_session import Session
import redis

from app.env import SESSION_HOST,SESSION_PORT,SESSION_PWD,SESSION_DB, SESSION_TYPE

msession = Session()

#======
def configure(app):
    print('>>>Init SESSION')
    app.config['SESSION_TYPE'] = SESSION_TYPE
    app.config['SESSION_REDIS'] = redis.StrictRedis(host=SESSION_HOST,port=SESSION_PORT,password=SESSION_PWD,db=SESSION_DB)    
    msession.init_app(app)
    return msession
  
