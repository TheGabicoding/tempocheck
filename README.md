# Tempocheck

Projeto em Python que consulta o clima atual de uma cidade usando a API pública [Open-Meteo](https://open-meteo.com/) e salva o histórico das consultas em um banco de dados SQLite.

## Como funciona

1. O usuário digita o nome de uma cidade.
2. O script consulta a **API de Geocoding** do Open-Meteo para obter a latitude e longitude da cidade.
3. Com as coordenadas, o script consulta a **API de Forecast** do Open-Meteo e obtém a temperatura e a velocidade do vento atuais.
4. Os dados são salvos em uma tabela `registros_clima` no arquivo `clima.db` (criado automaticamente na primeira execução).
5. Ao final, o script exibe no terminal o histórico completo de todas as consultas já salvas no banco.

## Estrutura da tabela

| Coluna       | Tipo     | Descrição                                  |
|--------------|----------|---------------------------------------------|
| id           | INTEGER  | Identificador único (gerado automaticamente) |
| cidade       | TEXT     | Nome da cidade consultada                   |
| latitude     | REAL     | Latitude da cidade                          |
| longitude    | REAL     | Longitude da cidade                         |
| temperatura  | REAL     | Temperatura atual (°C)                      |
| vento        | REAL     | Velocidade do vento atual (km/h)            |
| data_hora    | TEXT     | Data e hora da consulta                     |

## Pré-requisitos

- Python 3.8 ou superior
- Biblioteca `requests`

## Instalação

```bash
pip install requests
```

> O módulo `sqlite3` já vem incluso no Python, não é necessário instalar nada além do `requests`.

## Como executar

```bash
python main.py
```

Digite o nome da cidade quando solicitado. O script vai imprimir o clima atual e o histórico de todas as consultas já realizadas.

### Exemplo de execução

```
Digite a cidade que deseja acompanhar: Recife
Recife: 27.3°C, vento 12.1 km/h
Dados salvos com sucesso!

--- Histórico salvo no banco ---
2026-08-12 14:32:10 | Recife: 27.3°C, vento 12.1 km/h
2026-08-11 09:15:42 | Caruaru: 24.8°C, vento 8.4 km/h
```

## Visualizando o banco de dados diretamente

Como os dados ficam salvos em um arquivo `clima.db`, é possível visualizá-los sem precisar rodar o script:

- **DB Browser for SQLite** (interface gráfica): [sqlitebrowser.org](https://sqlitebrowser.org/)
- **Terminal**: `sqlite3 clima.db` e depois `SELECT * FROM registros_clima;`
- **VS Code**: extensão *SQLite Viewer*

## Possíveis melhorias futuras

- Migrar o armazenamento para MySQL ou PostgreSQL.
- Adicionar agendamento para coletar o clima automaticamente em intervalos definidos.
- Gerar gráficos de histórico com `matplotlib`.
- Usar variáveis de ambiente para configurações sensíveis, caso o projeto evolua para usar um banco externo.
