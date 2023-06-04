from pydantic import BaseSettings, BaseModel, SecretStr, PostgresDsn, RedisDsn


class Postgres(BaseModel):
    dsn: PostgresDsn


class Redis(BaseModel):
    dsn: RedisDsn


class Settings(BaseSettings):
    bot_token: SecretStr
    owner_id: int

    postgres: Postgres
    redis: Redis

    class Config:
        env_file = ".env"
        env_nested_delimiter = "_"


config = Settings()
