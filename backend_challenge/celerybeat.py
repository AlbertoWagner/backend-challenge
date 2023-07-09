from celery import Celery
from django.conf import settings

app = Celery('backend_challenge')
app.config_from_object(settings, namespace='CELERY')
app.conf.beat_schedule = {
    # Defina aqui as tarefas agendadas
}
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
