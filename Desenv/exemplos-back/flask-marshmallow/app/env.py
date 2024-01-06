
import dotenv
import json
import os

dotenv_path = '.env'
dotenv.load_dotenv(dotenv_path)

#=====================================================================
SECRET_KEY = os.getenv('SECRET_KEY')

#=====================================================================
DEBUG = os.getenv('DEBUG')
DEBUG_QUERY = int(os.getenv('DEBUG_QUERY'))

#=====================================================================   
DB_URL = os.getenv('DB_URL')

#=====================================================================   
SESSION_TYPE = os.getenv('SESSION_TYPE')
SESSION_HOST = os.getenv('SESSION_HOST')
SESSION_PORT = os.getenv('SESSION_PORT')
SESSION_PWD = os.getenv('SESSION_PWD')
SESSION_DB = os.getenv('SESSION_DB')

#=====================================================================   
MAIL_SMTP_HOST=os.getenv('MAIL_SMTP_HOST')
MAIL_SMTP_PORT=int(os.getenv('MAIL_SMTP_PORT'))
MAIL_SMTP_USER=os.getenv('MAIL_SMTP_USER')
MAIL_SMTP_PWD=os.getenv('MAIL_SMTP_PWD')

#=====================================================================   
STORAGE_UPLOAD_FOLDER=os.getenv('STORAGE_UPLOAD_PATH')

