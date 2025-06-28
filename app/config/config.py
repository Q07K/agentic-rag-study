from pydantic_settings import BaseSettings, SettingsConfigDict


class AppConfig(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
    )

    sqlite_db_path: str
    encryption_key: bytes


if __name__ == "__main__":
    config = AppConfig()
    print(type(config.encryption_key))
    print(f"{config.encryption_key = }")
