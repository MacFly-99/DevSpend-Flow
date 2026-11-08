from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    PROJECT_NAME: str = "DevSpend-Flow"
    VERSION: str = "0.1.0"
    API_V1_STR: str = "/api/v1"
    DATABASE_URL: str = "sqlite:///./devspend.db"

    # Cette ligne dit à Pydantic d'aller lire le fichier .env
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

# On instancie les settings pour pouvoir les importer partout
settings = Settings()