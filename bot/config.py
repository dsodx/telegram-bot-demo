from pydantic import BaseSettings, BaseModel, SecretStr, PostgresDsn


class Postgres(BaseModel):
    dsn: PostgresDsn


class Settings(BaseSettings):
    bot_token: SecretStr
    owner_id: int

    postgres: Postgres

    class Config:
        env_file = ".env"
        env_nested_delimiter = "_"


config = Settings()
