import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config():
    CONFIG_KEY = os.environ.get('CONFIG_KEY') or 'failed to get a unique one'
    SQLALCHEMY_DATABASE_URI = f'sqlite:///{os.path.join(basedir, "weatherData.db")}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    CELERY_BROKER_URL = 'redis://localhost:7777/0'
    CELERY_RESULT_BACKEND = 'redis://localhost:7777/0'
