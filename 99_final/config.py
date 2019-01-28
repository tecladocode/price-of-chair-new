import os

DEBUG = True
ADMIN = os.environ.get('APP_ADMIN')
MAILGUN_URL = os.environ.get('MAILGUN_URL')
MAILGUN_API_KEY = os.environ.get('MAILGUN_API_KEY')
MAILGUN_FROM = os.environ.get('MAILGUN_FROM')
ALERT_TIMEOUT = 10