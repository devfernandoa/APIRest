# API REST com FastAPI e PostgreSQL

Bem-vindo à documentação da API REST construída com FastAPI e PostgreSQL. Esta documentação fornece informações sobre como usar a API e seus endpoints.

## Visão Geral

Esta API permite que os usuários registrem-se, façam login e consultem dados meteorológicos. A API é construída usando FastAPI e PostgreSQL, e é executada em contêineres Docker.

## Endpoints

- [Registrar](docs/registrar.md)
- [Login](docs/login.md)
- [Consultar](docs/consultar.md)

## Configuração e Execução

### Pré-requisitos

- Docker
- Docker Compose

### Passos para executar o projeto

1. Clone o repositório:
   ```
   git clone https://github.com/devfernandoa/APIRest/
    ```
2. Acesse o diretório do projeto:
   ```
   cd APIRest
    ```
3. Rode o docker-compose:
   ```
   docker-compose up
    ```
4. Accesse a documentação da API em:
   ```
   http://localhost:8000/docs
    ```