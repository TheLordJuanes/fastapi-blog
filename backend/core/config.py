import os
from dotenv import load_dotenv

from pathlib import Path
env_path = Path('') / '.env'
load_dotenv(dotenv_path=env_path)

class Settings:
    # Project Environment Variables
    PROJECT_TITLE: str = "Blog API"
    PROJECT_VERSION: str = "0.1.0"

    # Postgres Environment Variables
    POSTGRES_USER: str = os.getenv("POSTGRES_USER")
    POSTGRES_PASSWORD: str = os.getenv("POSTGRES_PASSWORD")
    POSTGRES_SERVER: str = os.getenv("POSTGRES_SERVER", "localhost")
    POSTGRES_PORT: int = os.getenv("POSTGRES_PORT", 5432)
    POSTGRES_DB: str = os.getenv("POSTGRES_DB")
    DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}:{POSTGRES_PORT}/{POSTGRES_DB}"

settings = Settings()