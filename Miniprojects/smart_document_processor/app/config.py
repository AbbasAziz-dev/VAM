import os
from dotenv import load_dotenv

load_dotenv()


class Settings:
    LANGUAGE_API_URL: str = os.getenv("LANGUAGE_API_URL")
    LANGUAGE_API_KEY: str = os.getenv("LANGUAGE_API_KEY")
    QUOTE_API_URL: str = os.getenv("QUOTE_API_URL")


settings = Settings()