README.md

# Product Sync Challenge

Este é um desafio proposto pela Coodesh para sincronização de produtos.

## Descrição do Projeto

O projeto consiste em desenvolver uma aplicação que realiza a sincronização de produtos a partir de uma fonte externa, utilizando web scraping. A aplicação busca os dados dos produtos de um site específico, processa esses dados e os armazena em um banco de dados.

## Tecnologias Utilizadas

- Python
- Django
- Django REST Framework
- PostgreSQL
- Celery
- Redis
- Docker

## Instalação e Uso

Siga as instruções abaixo para instalar e executar o projeto:

1. Clone o repositório para sua máquina local:

   ```shell
   git clone https://github.com/AlbertoWagner/backend-challenge.git
   ```

2. Navegue até o diretório do projeto:

   ```shell
   cd backend-challenge
   ```


3. Configure as variáveis de ambiente no arquivo `.env`:

   ```
      SECRET_KEY=django-insecure-o$pcu!s$tbml==0fjfeo%$(92^!13hv#p7qckma)p03_t^*j&z
      DEBUG=True
      SITE_ID=1
      ALLOWED_HOSTS=*
      
      DB_NAME=mydatabase
      DB_USER=myuser
      DB_PASSWORD=mypassword
      DB_HOST=db
      DB_PORT=5432
      
      DJANGO_SETTINGS_MODULE=backend_challenge.settings
      CELERY_BROKER_URL=redis://redis:6379/0
      CELERY_RESULT_BACKEND=redis://redis:6379/0
      
      CELERY_BROKER_URL=redis://redis:6379/0
      CELERY_RESULT_BACKEND=redis://redis:6379/0
      POSTGRES_HOST_AUTH_METHOD=trust
      
      POSTGRES_USER=myuser
      POSTGRES_PASSWORD=mypassword
      POSTGRES_DB=mydatabase
      
      DJANGO_SUPERUSER_USERNAME=admin
      DJANGO_SUPERUSER_EMAIL=admin@example.com
      DJANGO_SUPERUSER_PASSWORD=admin
   ```
   
4. Crie e inicie os contêineres Docker:

  ```
      docker-compose up --build
  ```

5. Aguarde até que todos os serviços estejam em execução. Você verá logs indicando o progresso.

6. Acesse a aplicação em seu navegador em http://localhost:8080/.

7. Para executar os testes, você pode usar o seguinte comando:

 ```
     docker exec -it backend-challenge-web-1 python manage.py test
  ```


## REST API

A aplicação possui uma REST API para acessar e gerenciar os produtos. Abaixo estão os principais endpoints da API:

- `GET /`: Retorna uma mensagem de boas-vindas indicando que a API está funcionando corretamente.
- `GET /products/`: Lista todos os produtos disponíveis.
- `GET /products/{code}/`: Obtém informações de um produto específico com base no código.

Exemplo de resposta para o endpoint `GET /products/{code}/`:

```json
{
  "code": "3251490332080",
  "barcode": "0462245783733",
  "status": "imported",
  "imported_t": "2023-07-09T00:53:57Z",
  "url": "https://www.example.com/product/3251490332080",
  "product_name": "Product Name",
  "quantity": "100",
  "categories": ["category1", "category2"],
  "packaging": ["packaging1", "packaging2"],
  "brands": "Brand",
  "image_url": "https://www.example.com/images/product/3251490332080.jpg"
}
```


## Cron Job

Foi configurado um cron job para executar a sincronização dos produtos em um horário específico todos os dias. O cron job está agendado para rodar às 23:30h.

O objetivo do cron job é buscar os dados dos produtos da fonte externa, processá-los e armazená-los no banco de dados. Dessa forma, a base de dados estará sempre atualizada com as informações mais recentes.

Este projeto foi desenvolvido como parte do desafio proposto pela Coodesh.


## Agradecimentos

Agradecemos à Coodesh por propor esse desafio interessante.

## Contato

Se tiver alguma dúvida ou sugestão, entre em contato:

- [E-mail](mailto:seu-email@example.com)
- [LinkedIn](https://www.linkedin.com/in/seu-perfil-linkedin)

---

Este projeto foi desenvolvido como parte do desafio proposto pela Coodesh.

Para mais informações sobre o desafio, visite [Coodesh](https://coodesh.com/).


<a href="#">
 <sub><b>Alberto Wagner</b></sub></a> <a href="#" ></a>


Feito por Alberto 👋🏽 Entre em contato!

[![Linkedin Badge](https://img.shields.io/badge/-Alberto-blue?style=flat-square&logo=Linkedin&logoColor=white&link=https://www.linkedin.com/in/alberto-wagner-5571a3106/)](https://www.linkedin.com/in/alberto-wagner-5571a3106/)
[![Gmail Badge](https://img.shields.io/badge/-albertow475@gmail.com-c14438?style=flat-square&logo=Gmail&logoColor=white&link=mailto:albertow475@gmail.com)](mailto:albertow475@gmail.com
)
