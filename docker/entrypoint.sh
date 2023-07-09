#!/bin/sh

set -e # sai se ocorrerem erros em qualquer lugar

# Coleta de arquivos estáticos
python manage.py collectstatic --noinput

python manage.py makemigrations

# Executa migrações do banco de dados
python manage.py migrate

# Inicia o servidor Django
python manage.py runserver 0.0.0.0:8080
