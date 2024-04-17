from dataclasses import dataclass
from environs import Env


@dataclass
class APIConfig:
    google_api: str  # Токен для доступа к API Google
    yandex_api: str  # Токен для доступа к API Yandex Cloud
    yandex_catalogue_id: str  # Идентификатор каталога Yandex Cloud


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
    return Config(tg_bot=TgBot(token=env('BOT_TOKEN')),
                  api_config=APIConfig(google_api=env('GGL_API_KEY'),
                                       yandex_api=env('YDX_CLOUD_API_KEY'),
                                       yandex_catalogue_id=env('YDX_CLOUD_CATALOGUE_ID')))
