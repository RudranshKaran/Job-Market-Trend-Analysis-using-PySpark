from __future__ import annotations

import streamlit as st
from pyspark.sql import DataFrame, SparkSession
from pyspark.sql import functions as F

from app.components.charts import bar_chart, pie_chart
from app.components.layout import render_page_header
from app.components.metrics import render_metric_cards
from app.components.theme import apply_theme
from app.utils.app_state import get_spark, load_data_or_stop


REQUIRED_COLUMNS = ["remote_ratio", "salary_in_usd"]


def _validate_columns(df) -> bool:
    missing = [col for col in REQUIRED_COLUMNS if col not in df.columns]
    if missing:
        st.error(f"Missing required columns: {', '.join(missing)}")
        return False
    return True


def render_page(df: DataFrame | None = None, spark: SparkSession | None = None) -> None:
    apply_theme()
    if df is None:
        df = load_data_or_stop()
    if spark is None:
        spark = get_spark()

    render_page_header(
        "Remote Work Analysis",
        "Understand remote, hybrid, and onsite job trends.",
        "Flexibility",
        ["Onsite vs Remote", "Salary impact"],
    )

    if not _validate_columns(df):
        return

    total_jobs = df.count()
    remote_count = df.filter(F.col("remote_ratio") == 100).count()
    remote_pct = (remote_count / total_jobs * 100) if total_jobs else 0

    metrics = [
        {"label": "Total Jobs", "value": f"{total_jobs:,}", "subtitle": "All roles"},
        {"label": "Fully Remote", "value": f"{remote_pct:,.1f}%", "subtitle": "Remote ratio = 100"},
    ]
    render_metric_cards(metrics)

    st.divider()
    remote_dist = df.groupBy("remote_ratio").count().orderBy("remote_ratio").toPandas()
    remote_dist["remote_label"] = remote_dist["remote_ratio"].map(
        {0: "Onsite", 50: "Hybrid", 100: "Fully Remote"}
    )

    col_left, col_right = st.columns([1, 1])
    with col_left:
        st.subheader("Remote Mix")
        fig = pie_chart(
            remote_dist,
            labels="remote_label",
            values="count",
            title="Remote vs Hybrid vs Onsite",
        )
        if fig:
            st.pyplot(fig, use_container_width=True)

    with col_right:
        st.subheader("Remote Job Counts")
        fig = bar_chart(
            remote_dist,
            x="remote_label",
            y="count",
            title="Job Count by Remote Ratio",
            xlabel="Work Mode",
            ylabel="Jobs",
        )
        if fig:
            st.pyplot(fig, use_container_width=True)

    st.divider()
    st.subheader("Salary by Remote Ratio")
    salary_remote = (
        df.groupBy("remote_ratio")
        .agg(F.avg("salary_in_usd").alias("avg_salary_usd"))
        .orderBy("remote_ratio")
        .toPandas()
    )
    salary_remote["remote_label"] = salary_remote["remote_ratio"].map(
        {0: "Onsite", 50: "Hybrid", 100: "Fully Remote"}
    )
    fig = bar_chart(
        salary_remote,
        x="remote_label",
        y="avg_salary_usd",
        title="Average Salary by Remote Ratio",
        xlabel="Work Mode",
        ylabel="Avg Salary (USD)",
    )
    if fig:
        st.pyplot(fig, use_container_width=True)

    st.divider()
    st.subheader("Insights")
    st.markdown(
        """
        <div class="insight-list">
        <ul>
            <li>Fully remote roles remain competitive with onsite salaries.</li>
            <li>Hybrid roles often sit between onsite and remote compensation ranges.</li>
            <li>Remote work continues to be a major hiring pattern across roles.</li>
        </ul>
        </div>
        """,
        unsafe_allow_html=True,
    )


render_page()
