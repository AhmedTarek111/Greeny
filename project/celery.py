import os

from celery import Celery,shared_task

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')

app = Celery('proj')


app.config_from_object('django.conf:settings', namespace='CELERY')


app.autodiscover_tasks()


