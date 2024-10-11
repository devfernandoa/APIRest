# Endpoint: Login

## Descrição

Autentica um usuário na aplicação.

## URL

`/login`

## Método HTTP

`POST`

## Parâmetros

- [`email`]("Go to definition"): Email do usuário (string)
- [`senha`]("Go to definition"): Senha do usuário (string)

## Exemplo de Requisição

```json
{
    "email": "cloud@insper.edu.br",
    "senha": "cloud0"
}
```

## Exemplo de Resposta

```json
{
    "jwt": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.
            eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkRpc2N
            pcGxpbmEgQ2xvdWQiLCJpYXQiOjE1MTYyMzkwMjJ9.
            s76o9X4UIANSI-aTF8UhqnBYyIRWw_WH4ut8Xqmo6i0"
}
```

## GIF do funcionamento

![Exemplo Login](ExemploLogin.gif)
1
