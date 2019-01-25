import os

DEBUG = True
ADMINS = frozenset(['jslvtr@gmail.com'])
MAILGUN_URL = os.environ.get('MAILGUN_URL')
MAILGUN_API_KEY = os.environ.get('MAILGUN_API_KEY')
MAILGUN_FROM = os.environ.get('MAILGUN_FROM')
ALERT_TIMEOUT = 10