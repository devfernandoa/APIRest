# Endpoint: Consultar

## Descrição

Consulta dados meteorológicos (requer autenticação).

## URL

`/consultar`

## Método HTTP

`GET`

## Cabeçalhos

- `Authorization`: Bearer token_jwt_aqui

## Exemplo de Resposta

```json
{
  "latitude": -46.67,
  "longitude": -23.59,
  "timezone": "America/Sao_Paulo",
  "current": {
    "time": "2023-10-01T00:00:00Z",
    "temperature_2m": 25.0,
    "wind_speed_10m": 5.0
  },
  "hourly": [
    {
      "time": "2023-10-01T01:00:00Z",
      "temperature_2m": 24.0
    },
    {
      "time": "2023-10-01T02:00:00Z",
      "temperature_2m": 23.0
    }
  ]
}
```

## Print do funncionamento

![Exemplo Registrar](ExemploRegistrarWhite.png#only-light)
![Exemplo Registrar](ExemploRegistrarDark.png#only-dark)
