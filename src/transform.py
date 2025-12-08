import pandas as pd
import numpy as np
from src.utils import log
from config.settings import PROCESSED_DATA_PATH,COLUMN_MAP,ZERO_TO_NAN_COLS,RANGE_RULES



def transform_data(df: pd.DataFrame) -> pd.DataFrame:
    log("🧹 Transform 시작")
    if COLUMN_MAP:
        df = df.rename(columns=COLUMN_MAP)

    if "id" in df.columns:
        df["id"] = df["id"].astype(str).str.strip()
        df = df[df["id"] != ""]


    for col in ZERO_TO_NAN_COLS:
        if col in df.columns:
            df[col] = df[col].replace(0, np.nan)

    for col, (low, high) in RANGE_RULES.items():
        if col in df.columns:
            df.loc[(df[col] < low) | (df[col] > high), col] = np.nan

    num_cols = df.select_dtypes(include=["number"]).columns
    df[num_cols] = df[num_cols].fillna(df[num_cols].median())
    return df


def save_processed(df: pd.DataFrame):
    df.to_csv(PROCESSED_DATA_PATH, index=False)
    log(f"📁 Transform 완료 — 파일 저장: {PROCESSED_DATA_PATH}")
