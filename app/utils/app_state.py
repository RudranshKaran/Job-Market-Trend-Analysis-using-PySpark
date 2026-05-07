from __future__ import annotations

from pathlib import Path

import streamlit as st
from pyspark.sql import DataFrame, SparkSession

from app.components.layout import render_page_header
from app.utils.spark_session import get_spark_session

PROJECT_ROOT = Path(__file__).resolve().parents[2]
DATA_PATH = PROJECT_ROOT / "data" / "processed" / "cleaned_jobs"


@st.cache_resource
def get_spark() -> SparkSession:
    return get_spark_session(app_name="Job Market Trends Dashboard")


@st.cache_resource
def load_processed_data(path: str) -> DataFrame:
    spark = get_spark()
    return spark.read.parquet(path)


def load_data_or_stop() -> DataFrame:
    if not DATA_PATH.exists() or not any(DATA_PATH.rglob("*.parquet")):
        render_page_header("Data Not Ready", "Run preprocessing to generate cleaned data.", "Setup")
        st.warning("Processed dataset not found in the expected location.")
        st.code("python scripts/run_preprocessing.py", language="bash")
        st.info(f"Expected parquet directory: {DATA_PATH}")
        st.stop()

    return load_processed_data(str(DATA_PATH))
