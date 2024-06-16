from pydantic_settings import BaseSettings, SettingsConfigDict

from functools import lru_cache

# .envなどの環境変数を扱うSettingsモデル
# https://fastapi.tiangolo.com/advanced/settings/?h=environ#reading-a-env-file
class Settings(BaseSettings):
    app_name: str = "Awesome API"
    expected_aud: str
    iss: str

    model_config = SettingsConfigDict(env_file=".env")

@lru_cache
def get_settings():
    return Settings()