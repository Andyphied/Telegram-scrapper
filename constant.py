import os
from dotenv import load_dotenv
from pathlib import Path

path = Path.cwd()
env_path = path / ".env"
load_dotenv(env_path)

APP_ID = os.environ["APP_ID"]

API_HASH = os.environ["API_HASH"]

PHONE_NO = os.environ["PHONE_NO"]

PASSWORD = os.environ["PASSWORD"]