# API REST com FastAPI e PostgreSQL

Este projeto é uma API REST construída com FastAPI e PostgreSQL. A API permite registrar usuários, autenticar e consultar dados meteorológicos.

[Acesse a documentação aqui!](https://devfernandoa.github.io/APIRest)

[Imagem no Docker Hub](https://hub.docker.com/repository/docker/devfernandoa/apirest)

[Video de Demonstração](https://www.youtube.com/watch?v=dQw4w9WgXcQ)

## Informações sobre o projeto

O projeto possui três endpoints principais:

- Registrar
- Login
- Consultar

O endpoint de registrar permite que um usuário se registre na aplicação. O endpoint de login permite que um usuário autentique-se na aplicação. O endpoint de consultar permite que um usuário autenticado consulte dados meteorológicos, obtidos na API [open-meteo](https://open-meteo.com/), com a localização do Insper.

Para mais informações sobre como utilizar o projeto, [acesse a documentação aqui!](https://devfernandoa.github.io/APIRest)

## Pré-requisitos

- Docker
- Docker Compose

## Configuração e Execução

### Passos para executar o projeto

1. Clone o repositório:

   ```sh
   git clone https://github.com/devfernandoa/APIRest.git
   ```

2. Acesse o diretório do projeto:

   ```sh
   cd APIRest
   ```

3. Rode o docker-compose:

   ```sh
   docker-compose up
   ```

4. Accesse a documentação da API em:

   ```sh
   http://localhost:8000/docs
   ```

## Autoria

Feito por: Fernando Alzueta

O projeto foi desenvolvido como parte do curso de Computação em Nuvem do Insper. 
