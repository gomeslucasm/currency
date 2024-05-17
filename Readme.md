# API de conversão monetária

Este projeto é uma API de conversão monetária desenvolvida com FastAPI, que permite converter valores entre diferentes moedas usando taxas de câmbio reais e atualizadas.

## Componentes do Projeto

- **API de Conversão Monetária**: Implementada usando FastAPI.
- **Exchange Rate API**: Utiliza a API [ExchangeRate-API](https://www.exchangerate-api.com) para obter as taxas de câmbio.
- **Docker e Docker Compose**: Para contêinerização e orquestração de contêineres.
- **Poetry**: Para gerenciamento de dependências.
- **Pytest**: Para testes unitários e geração de relatório de cobertura de código.

## Tecnologias Necessárias

Para rodar este projeto, você precisará das seguintes tecnologias instaladas em seu ambiente:

- Docker
- Docker Compose
- Make

## Como Rodar o App

O projeto inclui um `Makefile` que simplifica a execução de comandos comuns. Aqui estão os comandos disponíveis:

- **Build**: Constrói as imagens Docker.

```bash
  make build
```

- **Up**: Inicia os contêineres em modo destacado (background).

```bash
make up
```

## Como Usar a API

### Endpoint /api/convert

Este endpoint permite converter valores entre diferentes moedas. A requisição deve receber os seguintes parâmetros de query string:

- from: A moeda de origem.
- to: A moeda de destino.
- amount: O valor a ser convertido.

Exemplo de requisição:

```bash
curl -X GET "http://localhost:8000/api/convert?from=USD&to=EUR&amount=100"

```

## Documentação da api

A documentação Swagger da API está disponível em /docs. Você pode acessar esta documentação para visualizar e testar os endpoints da API.

http://localhost/docs

## Como Rodar os Testes, Gerar Coverage e Ver o Coverage

Para rodar os testes e gerar o relatório de cobertura de código, utilize os seguintes comandos:

- Rodar os Testes: Executa os testes usando pytest.

```bash
make test
```

- Gerar Coverage: Executa os testes e gera o relatório de cobertura de código.

```bash
make coverage
```

- Ver o Coverage: Após gerar o relatório de cobertura, você pode abrir o arquivo htmlcov/index.html em seu navegador para ver o relatório detalhado.
