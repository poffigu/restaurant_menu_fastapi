import os
from dotenv import load_dotenv


load_dotenv()

POSTGRES_HOST = os.environ.get('POSTGRES_HOST')
POSTGRES_PORT = os.environ.get('POSTGRES_PORT')
POSTGRES_DB = os.environ.get('POSTGRES_DB')
POSTGRES_USER = os.environ.get('POSTGRES_USER')
POSTGRES_PASSWORD = os.environ.get('POSTGRES_PASSWORD')

DATABASE_URL = (f"postgresql+asyncpg://{POSTGRES_USER}:{POSTGRES_PASSWORD}" f"@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}")
