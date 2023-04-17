from dataclasses import dataclass
from environs import Env


@dataclass
class APIConfig:
    google_api: str  # Название базы данных


@dataclass
class TgBot:
    token: str  # Токен для доступа к телеграм-боту


@dataclass
class Config:
    tg_bot: TgBot
    api_config: APIConfig


def load_config(path: str | None = None) -> Config:
    env = Env()
    env.read_env(path)
    return Config(tg_bot=TgBot(token=env('bot_token')),
                  api_config=APIConfig(google_api=env('ggl_api_key')))
