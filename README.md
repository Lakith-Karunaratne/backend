## DB STRING

Change this and use for prod
`sqlalchemy.url = postgresql+psycopg2://admin_db:abcd1234@localhost:5432/dev_db`

## Migrations

To make and Track Migrations

`alembic revision --autogenerate -m "Change name"`

`alembic upgrade head`

## Secret Generator

`import os; print(os.urandom(24).hex())`

