from __future__ import annotations

from pathlib import Path
import sys

import streamlit as st

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from app.components.sidebar import render_sidebar
from app.pages import (
    dashboard,
    experience_analysis,
    location_analysis,
    remote_work_analysis,
    salary_analysis,
)
from app.utils.spark_session import get_spark_session

DATA_PATH = Path("data") / "processed" / "cleaned_jobs"

st.set_page_config(
    page_title="Job Market Trends Dashboard",
    page_icon="📊",
    layout="wide",
)


def _apply_theme() -> None:
    css = """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;600;700&display=swap');

    html, body, [class*="css"] {
        font-family: 'Space Grotesk', sans-serif;
    }

    .stApp {
        background: linear-gradient(135deg, #f6f7fb 0%, #eef6f5 50%, #fff4e6 100%);
    }

    .section-card {
        background: #ffffff;
        border: 1px solid #e6eaf0;
        border-radius: 12px;
        padding: 1.2rem;
        box-shadow: 0 6px 18px rgba(10, 20, 30, 0.06);
    }

    .kpi-card {
        background: #ffffff;
        border: 1px solid #e7edf4;
        border-radius: 14px;
        padding: 1rem 1.2rem;
        box-shadow: 0 6px 16px rgba(20, 30, 40, 0.08);
    }

    .kpi-label {
        color: #4b5563;
        font-size: 0.85rem;
        text-transform: uppercase;
        letter-spacing: 0.08em;
        font-weight: 600;
        margin-bottom: 0.3rem;
    }

    .kpi-value {
        color: #111827;
        font-size: 1.6rem;
        font-weight: 700;
    }

    .kpi-sub {
        color: #6b7280;
        font-size: 0.85rem;
        margin-top: 0.25rem;
    }
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)


@st.cache_resource
def get_spark() -> object:
    return get_spark_session(app_name="Job Market Trends Dashboard")


@st.cache_resource
def load_processed_data(path: str):
    spark = get_spark()
    return spark.read.parquet(path)


def _load_data_or_stop() -> object:
    if not DATA_PATH.exists():
        st.error(
            "Processed dataset not found. Run the preprocessing pipeline first:"
            " `python scripts/run_preprocessing.py`"
        )
        st.stop()

    return load_processed_data(str(DATA_PATH))


def main() -> None:
    _apply_theme()

    pages = {
        "Dashboard": dashboard.render_page,
        "Salary Analysis": salary_analysis.render_page,
        "Remote Work Analysis": remote_work_analysis.render_page,
        "Experience Analysis": experience_analysis.render_page,
        "Location Analysis": location_analysis.render_page,
    }

    selection = render_sidebar(list(pages.keys()))
    df = _load_data_or_stop()
    spark = get_spark()

    pages[selection](df, spark)


if __name__ == "__main__":
    main()
