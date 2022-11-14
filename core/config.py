import os
from dotenv import load_dotenv
from pathlib import Path

# env_path = Path('.') / '.env'
load_dotenv()


class Settings:

    PROJECT_NAME: str = "TSORT"
    PROJECT_VERSION: str = "1.0.0"
    PROJECT_KEY = os.getenv("DETA_PROJECT_KEY")


settings = Settings()
