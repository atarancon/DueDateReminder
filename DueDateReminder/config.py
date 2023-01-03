import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'secret-key'
    #SQLALCHEMY_DATABASE_URI = os.environ.get(' sqlite:///bill_list.db')
    MAIL_SERVER = os.environ.get('MAIL_SERVER') or 'smtp.gmail.com'
    MAIL_PORT = int(os.environ.get('MAIL_PORT') or 587)
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS') or True
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME') or 'user@example.com'
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD') or 'password'
    SMS_API_KEY = os.environ.get('SMS_API_KEY') or 'api-key'
    SMS_API_SECRET = os.environ.get('SMS_API_SECRET') or 'api-secret'
