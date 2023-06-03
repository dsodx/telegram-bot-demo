# Telegram Bot Demo
## Setup
Fill and rename this files:
```
│   .env.dist
│   alembic.ini.dist
│
├───psql
│       .env.dist
```
Then run:
```shell
# first run:
# docker compose up -d postgres
# docker compose run bot alembic upgrade head
docker compose up -d
```
## Stack:
* Python 3.11.3
* PostgreSQL 15.2
* Aiogram 3.0.0b7
* SQLAlchemy 2.0.15
* Asyncpg 0.27.0 (as db driver)
### ENJOY!
