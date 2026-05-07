from __future__ import annotations

from pathlib import Path
import sys

import streamlit as st

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from pyspark.sql import functions as F

from app.components.layout import render_page_header
from app.components.theme import apply_theme
from app.components.metrics import render_metric_cards
from app.utils.app_state import get_spark, load_data_or_stop

st.set_page_config(
    page_title="Job Market Trends Dashboard",
    page_icon="📊",
    layout="wide",
)


def main() -> None:
    apply_theme()

    render_page_header(
        "Job Market Trends",
        "Interactive analytics powered by PySpark",
        "Home",
        ["Overview", "KPIs", "Trends"],
    )
    st.caption("Use the sidebar to switch between Dashboard, Salary, Remote Work, Experience, and Location pages.")

    df = load_data_or_stop()
    get_spark()

    total_jobs = df.count()
    avg_salary = df.select(F.avg("salary_in_usd").alias("avg_salary")).collect()[0][0] or 0
    countries = df.select("company_location").distinct().count()

    metrics = [
        {"label": "Total Jobs", "value": f"{total_jobs:,}", "subtitle": "Records in dataset"},
        {"label": "Average Salary", "value": f"${avg_salary:,.0f}", "subtitle": "USD"},
        {"label": "Countries", "value": f"{countries}", "subtitle": "Company locations"},
    ]

    render_metric_cards(metrics)

    st.divider()
    st.markdown(
        """
        **How to use the dashboard**

        - **Dashboard:** high-level KPIs and hiring trends.
        - **Salary Analysis:** top roles, distributions, and pay bands.
        - **Remote Work Analysis:** onsite vs hybrid vs remote trends.
        - **Experience Analysis:** seniority mix and salary comparisons.
        - **Location Analysis:** top hiring countries and salary hotspots.
        """
    )


if __name__ == "__main__":
    main()
