import os
import django
from django.contrib.auth import get_user_model

# Configurar as variáveis de ambiente do Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "backend_challenge.settings")
django.setup()

User = get_user_model()

if not User.objects.filter(username='admin').exists():
    username = os.environ.get('DJANGO_SUPERUSER_USERNAME', 'admin')
    email = os.environ.get('DJANGO_SUPERUSER_EMAIL', '')
    password = os.environ.get('DJANGO_SUPERUSER_PASSWORD', 'admin')
    print('****************************************************')
    User.objects.create_superuser(username=username, email=email, password=password)
