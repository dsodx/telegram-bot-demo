# Telegram Bot Demo
## Setup
Fill and rename this files:
```
├── .env
├── alembic.ini
├── psql
│   ├── .env
```
Then run:
```shell
docker compose build
# first run:
# docker compose up -d postgres
# docker compose run bot alembic upgrade head
docker compose up -d
```
## Stack:
* Python 3.11.3
* Aiogram 3.0.0b7
* PostgreSQL 15.2
* SQLAlchemy 2.0.15
* Alembic 1.11.1
* Asyncpg 0.27.0 (as driver)
### ENJOY!
