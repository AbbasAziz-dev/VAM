import os
from dotenv import load_dotenv

load_dotenv()

APP_NAME = os.getenv("APP_NAME")
INPUT_FILE = os.getenv("INPUT_FILE")