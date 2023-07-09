# Imagem base
FROM python:3.9

# Configuração do diretório de trabalho
RUN mkdir /code
WORKDIR /code

RUN apt-get update && apt-get install -y apt-utils && rm -rf /var/lib/apt/lists/*
RUN apt-get update && \
    apt-get install -y locales && \
    sed -i -e 's/# pt_BR ISO-8859-1/pt_BR ISO-8859-1/' -e 's/# pt_BR.UTF-8 UTF-8/pt_BR.UTF-8 UTF-8/' /etc/locale.gen && \
    dpkg-reconfigure --frontend=noninteractive locales
# Copia os arquivos de requisitos para o diretório de trabalho
COPY requirements.txt .

# Instala as dependências do projeto
RUN pip install --no-cache-dir -r requirements.txt

# Copia os arquivos do projeto para o diretório de trabalho
COPY . .

# Comando para iniciar o Celery Beat
CMD ["celery", "-A", "backend_challenge", "beat", "-l", "info"]
