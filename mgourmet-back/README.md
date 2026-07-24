# M Gourmet API

API REST da M Gourmet, construída com FastAPI, SQLAlchemy assíncrono e PostgreSQL.

## Execução local

1. Copie `.env.example` para `.env` e ajuste os valores necessários.
2. Instale as dependências: `pip install -e ".[dev]"`.
3. Suba PostgreSQL e Redis: `docker compose up -d db redis`.
4. Aplique as migrations: `alembic upgrade head`.
5. Popule os dados iniciais: `python -m scripts.seed`.
6. Inicie a API: `uvicorn app.main:app --reload`.

No Windows, após a configuração inicial, também é possível iniciar a API com `run.bat`.

Swagger: `http://localhost:8000/docs`.

## Produtos

- `GET /api/v1/products`: paginação, filtro por `category`/`featured`, busca por `search` e ordenação por `name` ou `price`.
- `GET /api/v1/products/featured`
- `GET /api/v1/products/{product_id}`

## Kits

- `GET /api/v1/kits`: paginação e ordenação por `name`, `meals` ou `price`.
- `GET /api/v1/kits/{kit_id}`

## Conteúdo institucional

- `GET /api/v1/testimonials` e `GET /api/v1/testimonials/{testimonial_id}`
- `GET /api/v1/faqs` e `GET /api/v1/faqs/{faq_id}`
- `GET /api/v1/contact`
- `GET /api/v1/content/benefits`
- `GET /api/v1/content/how-it-works`

As listagens retornam `{ "items": [...], "meta": {...} }`. Os produtos usam os campos em camelCase esperados pelo front-end, como `imageUrl` e `nutrition`.

O seed é idempotente: ele cria somente registros ausentes e não sobrescreve conteúdo já administrado.
