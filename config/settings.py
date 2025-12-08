import os
from dotenv import load_dotenv

# 현재 settings.py 기준으로 상위 폴더에 .env 파일을 두고 읽는 구조
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# env 파일 로드
dotenv_path = os.path.join(BASE_DIR, ".env")
load_dotenv(dotenv_path)

# ---------------------------------------------------------
# 📌 공통 설정
# ---------------------------------------------------------
RAW_DATA_PATH = os.getenv("RAW_DATA_PATH")
PROCESSED_DATA_PATH = os.getenv("PROCESSED_DATA_PATH")
CHUNK_SIZE = int(os.getenv("CHUNK_SIZE", "50000"))

# ---------------------------------------------------------
# 📌 MySQL 설정 
# ---------------------------------------------------------
MYSQL_CONFIG = {
    "host": os.getenv("MYSQL_HOST"),
    "port": int(os.getenv("MYSQL_PORT", "3306")),
    "user": os.getenv("MYSQL_USER"),
    "password": os.getenv("MYSQL_PASSWORD"),
    "db": os.getenv("MYSQL_DB"),
    "charset": "utf8mb4",
}
MYSQL_TABLE = os.getenv("MYSQL_TABLE")



# ---------------------------------------------------------
# 📌 데이터 전처리 과정 
# ---------------------------------------------------------

SOURCE_COLS = [
    "ID", "나이", "키(cm)", "몸무게(kg)", "BMI", "시력", "충치",
    "공복 혈당", "혈압", "중성 지방", "혈청 크레아티닌", "콜레스테롤",
    "고밀도지단백", "저밀도지단백", "헤모글로빈", "요 단백", "간 효소율", "label"
]

TARGET_COLS = [
    "id", "age", "height", "weight", "BMI", "sight", "cavity",
    "FPG", "blood_pressure", "TG", "SCR", "cholesterol",
    "HDL", "LDL", "Hb", "PRO", "LFT", "label"
]


COLUMN_MAP = dict(zip(SOURCE_COLS, TARGET_COLS))

ZERO_TO_NAN_COLS = [
    "sight", "FPG", "blood_pressure", "TG", "SCR",
    "cholesterol", "Hb", "HDL", "LDL", "LFT"
]
RANGE_RULES = {
    "age": (1, 120),
    "height": (50, 250),
    "weight": (20, 250),
    "BMI": (10, 80),
    "sight": (0, 2.5),
    "FPG": (40, 400),
    "blood_pressure": (30, 250),
    "TG": (10, 1000),
    "SCR": (0.2, 3.0),
    "cholesterol": (50, 400),
    "HDL": (10, 120),
    "LDL": (40, 300),
    "Hb": (5, 20),
    "PRO": (0, 5),
    "LFT": (0.1, 10),
}



# ---------------------------------------------------------
# 📌 MongoDB 설정
# ---------------------------------------------------------
MONGO_URI = os.getenv("MONGO_URI")
MONGO_DB_NAME = os.getenv("MONGO_DB_NAME")
MONGO_COLLECTION = os.getenv("MONGO_COLLECTION")

# ---------------------------------------------------------
# 📌 DB 선택 옵션
# ---------------------------------------------------------
USE_MYSQL = os.getenv("USE_MYSQL", "false").lower() == "true"
USE_MONGO = os.getenv("USE_MONGO", "false").lower() == "true"
