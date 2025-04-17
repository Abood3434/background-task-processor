import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'taskapi.settings')

app = Celery('taskapi')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
