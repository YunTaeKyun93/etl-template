import pymysql
from src.utils import log
from config.settings import MYSQL_CONFIG, MYSQL_TABLE
import os
from dotenv import load_dotenv

def load_to_mysql(df):
    log("🗄️ Load 시작 — DB 적재")
    table = MYSQL_TABLE

    conn = pymysql.connect(**MYSQL_CONFIG)  # type: ignore
    cur = conn.cursor()
    
    cols = ", ".join(df.columns)
    placeholders = ", ".join(["%s"] * len(df.columns))
    sql = f"INSERT INTO {table} ({cols}) VALUES ({placeholders})"

    data = [tuple(row) for row in df.to_numpy()]

    try:
        cur.executemany(sql, data)
        conn.commit()
        log("✅ Bulk Insert 완료")
    except Exception as e:
        log(f"❌ Load 오류: {e}")
        conn.rollback()
    finally:
        cur.close()
        conn.close()
