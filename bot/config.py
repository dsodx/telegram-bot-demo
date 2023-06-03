from pydantic import BaseSettings, SecretStr


class Settings(BaseSettings):
    bot_token: SecretStr
    owner_id: int

    class Config:
        env_file = ".env"


config = Settings()
