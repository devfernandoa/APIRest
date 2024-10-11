# Endpoint: Login

## Descrição

Autentica um usuário na aplicação.

## URL

`/login`

## Método HTTP

`POST`

## Parâmetros

- [`email`](command:_github.copilot.openSymbolFromReferences?%5B%22%22%2C%5B%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2Fhome%2Ffernando%2F6%2Fcloud%2FAPIRest%2Fapp%2Fmain.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A26%2C%22character%22%3A4%7D%7D%5D%2C%229a1fa8cb-7ff2-40b9-bea5-50498f3a6989%22%5D "Go to definition"): Email do usuário (string)
- [`senha`](command:_github.copilot.openSymbolFromReferences?%5B%22%22%2C%5B%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2Fhome%2Ffernando%2F6%2Fcloud%2FAPIRest%2Fapp%2Fmain.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A27%2C%22character%22%3A4%7D%7D%5D%2C%229a1fa8cb-7ff2-40b9-bea5-50498f3a6989%22%5D "Go to definition"): Senha do usuário (string)

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

## Print do funncionamento

![Exemplo Login](ExemploLoginWhite.png#only-light)
![Exemplo Login](ExemploLoginDark.png#only-dark)
