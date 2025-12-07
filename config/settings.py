import os
from dotenv import load_dotenv

load_dotenv() 

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


RAW_DATA_PATH = os.path.join(BASE_DIR, "data/raw/data.csv")
PROCESSED_DATA_PATH = os.path.join(BASE_DIR, "data/processed/processed_data.csv")


DB_CONFIG = {
    "host": os.getenv("DB_HOST"),
    "port": int(os.getenv("DB_PORT", "3306")),
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASSWORD"),
    "db": os.getenv("DB_NAME"),
    "charset": "utf8mb4"
}

CHUNK_SIZE = 100_000
