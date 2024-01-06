import json
import dotenv
import os

dotenv_path = ".env"
dotenv.load_dotenv(dotenv_path)

# ====================================
SECRET_KEY = os.getenv("SECRET_KEY")

# ====================================
DEBUG = int(os.getenv("DEBUG"))
DEBUG_QUERY = int(os.getenv("DEBUG_QUERY"))

# ====================================
DB_USERNAME = os.getenv("DB_USERNAME")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_DATABASE = os.getenv("DB_DATABASE")

# ====================================
SESSION_TYPE = os.getenv("SESSION_TYPE")
SESSION_HOST = os.getenv("SESSION_HOST")
SESSION_PORT = os.getenv("SESSION_PORT")
SESSION_PWD = os.getenv("SESSION_PWD")
SESSION_DB = os.getenv("SESSION_DB")
# ====================================

RQ_DASHBOARD_REDIS_URL = os.getenv("RQ_DASHBOARD_REDIS_URL")
RQ_DASHBOARD_USERNAME = os.getenv("RQ_DASHBOARD_USERNAME")
RQ_DASHBOARD_PASSWORD = os.getenv("RQ_DASHBOARD_PASSWORD")
# ====================================

MAIL_SMTP_HOST = os.getenv("MAIL_SMTP_HOST")
MAIL_SMTP_PORT = int(os.getenv("MAIL_SMTP_PORT"))
MAIL_SMTP_USER = os.getenv("MAIL_SMTP_USER")
MAIL_SMTP_PWD = os.getenv("MAIL_SMTP_PWD")
MAIL_SMTP_FROM = os.getenv("MAIL_SMTP_FROM")

# ====================================
STORAGE_UPLOAD_FOLDER = os.getenv("STORAGE_UPLOAD_FOLDER")

# ====================================
REPORT_FOLDER = os.getenv("REPORT_FOLDER")

# ====================================
AUTH_GOOGLE_CLIENT_ID = os.getenv("AUTH_GOOGLE_CLIENT_ID")
AUTH_GOOGLE_CLIENT_SECRET = os.getenv("AUTH_GOOGLE_CLIENT_SECRET")

# ====================================
LOG_SENTRY_URL = os.getenv("LOG_SENTRY_URL")

# ====================================
VERSION_BUILD = os.getenv("VERSION_BUILD")

# ====================================
PUBLIC_URL = os.getenv("PUBLIC_URL")

# ====================================
WEBSITE_BRAND = os.getenv("WEBSITE_BRAND")
WEBSITE_BRAND_RESUME = os.getenv("WEBSITE_BRAND_RESUME")
WEBSITE_URL = os.getenv("WEBSITE_URL")

# ====================================
APP_ERP_URL = os.getenv("APP_ERP_URL")
APP_SERVER_URL = os.getenv("APP_SERVER_URL")

# ====================================
GOOGLE_API_CLIENT = json.loads(os.getenv("GOOGLE_API_CLIENT"))

# ====================================
CACHE_TIMEOUT = json.loads(os.getenv("CACHE_TIMEOUT"))

# ====================================
LANGUAGE_DEFAULT = os.getenv("LANGUAGE_DEFAULT")
