# Endpoint: Registrar

## Descrição

Registra um novo usuário na aplicação.

## URL

`/registrar`

## Método HTTP

`POST`

## Parâmetros

- `nome`: Nome do usuário (string)
- `email`: Email do usuário (string)
- `senha`: Senha do usuário (string)

## Exemplo de Requisição

```json
{
    "nome": "Disciplina Cloud",
    "email": "cloud@insper.edu.br",
    "senha": "cloud0"
}
```

## Exemplo de Resposta

```json
{
    "jwt": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkRpc2NpcGxpbmEgQ2xvdWQiLCJpYXQiOjE1MTYyMzkwMjJ9.s76o9X4UIANSI-aTF8UhqnBYyIRWw_WH4ut8Xqmo6i0"
}
```

## Print do funncionamento

![Exemplo Consultar](ExemploConsultarWhite.png#only-light)
![Exemplo Consultar](ExemploConsultarDark.png#only-dark)
