from enum import StrEnum

from pydantic import BaseSettings, BaseModel, SecretStr, PostgresDsn, RedisDsn


class FSMStorageType(StrEnum):
    MEMORY = "memory"
    REDIS = "redis"


class Postgres(BaseModel):
    dsn: PostgresDsn


class Redis(BaseModel):
    dsn: RedisDsn


class Settings(BaseSettings):
    bot_token: SecretStr
    owner_id: int

    postgres: Postgres
    redis: Redis | None
    fsm_storage_type: FSMStorageType

    class Config:
        env_file = ".env"
        env_nested_delimiter = "_"


config = Settings()
