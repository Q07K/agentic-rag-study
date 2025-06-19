from pydantic_settings import BaseSettings, SettingsConfigDict


class AppConfig(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
    )

    sqlite_db_path: str


config = AppConfig()

if __name__ == "__main__":
    print(type(config.sqlite_db_path))
    print(f"{config.sqlite_db_path = }")
