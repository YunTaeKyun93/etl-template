import pandas as pd
from config.settings import RAW_DATA_PATH, CHUNK_SIZE
from src.utils import log

def extract_csv():
    log(f"📥 Extract 시작 — 파일: {RAW_DATA_PATH}")

    try:
        chunks = pd.read_csv(RAW_DATA_PATH, chunksize=CHUNK_SIZE)
        log(f"CSV 파일을 {CHUNK_SIZE} 행 단위로 로딩합니다.")
        return chunks
    except Exception as e:
        log(f"❌ Extract 오류: {e}")
        raise
