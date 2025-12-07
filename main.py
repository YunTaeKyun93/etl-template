from src.extract import extract_csv
from src.transform import transform_data, save_processed
from src.load import load_to_db
from src.utils import log, memory_usage

def main():
    log("🚀 ETL Pipeline 시작")
    log(f"현재 메모리 사용량: {memory_usage()} MB")

    for chunk in extract_csv():
        log("📤 Chunk 데이터 처리중...")

        df = transform_data(chunk)
        save_processed(df)
        load_to_db(df)

    log("🎉 ETL Pipeline 전체 완료")

if __name__ == "__main__":
    main()
