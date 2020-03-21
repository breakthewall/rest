from celery import Celery
from config import config, Config

celery = Celery(__name__, broker=Config.CELERY_BROKER_URL)

def create_app(config_name):
    # ...
    celery.conf.update(app.config)
    # ...
    return app
