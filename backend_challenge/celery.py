import os
from celery import Celery

# Configura a definição do Celery
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend_challenge.settings')
app = Celery('backend_challenge')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')