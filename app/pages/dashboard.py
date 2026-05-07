from __future__ import annotations

import streamlit as st
from pyspark.sql import functions as F

from app.components.charts import bar_chart, pie_chart
from app.components.metrics import render_metric_cards
from app.utils import analytics


REQUIRED_COLUMNS = [
    "salary_in_usd",
    "job_title",
    "company_location",
    "remote_ratio",
]


def _validate_columns(df) -> bool:
    missing = [col for col in REQUIRED_COLUMNS if col not in df.columns]
    if missing:
        st.error(f"Missing required columns: {', '.join(missing)}")
        return False
    return True


def render_page(df, spark) -> None:
    st.title("Job Market Trends Dashboard")
    st.caption("Snapshot of job market metrics and high-level trends.")

    if not _validate_columns(df):
        return

    total_jobs = df.count()
    avg_salary = df.select(F.avg("salary_in_usd").alias("avg_salary")).collect()[0][0] or 0
    countries = df.select("company_location").distinct().count()
    remote_jobs = analytics.get_remote_jobs(df).count()
    remote_pct = (remote_jobs / total_jobs * 100) if total_jobs else 0

    top_role_row = analytics.get_most_common_job_titles(df, limit=1).collect()
    top_role = top_role_row[0][0] if top_role_row else "N/A"

    metrics = [
        {
            "label": "Total Jobs",
            "value": f"{total_jobs:,}",
            "subtitle": "Records in dataset",
        },
        {
            "label": "Average Salary",
            "value": f"${avg_salary:,.0f}",
            "subtitle": "USD (overall)",
        },
        {
            "label": "Countries",
            "value": f"{countries}",
            "subtitle": "Company locations",
        },
        {
            "label": "Remote Jobs",
            "value": f"{remote_pct:,.1f}%",
            "subtitle": "Fully remote share",
        },
        {
            "label": "Top Role",
            "value": top_role,
            "subtitle": "Most common job title",
        },
    ]

    render_metric_cards(metrics)
    st.divider()

    col_left, col_right = st.columns([2, 1])

    with col_left:
        st.subheader("Top Hiring Locations")
        top_locations = analytics.get_top_hiring_locations(df, limit=10).toPandas()
        fig = bar_chart(
            top_locations,
            x="company_location",
            y="count",
            title="Top 10 Hiring Countries",
            xlabel="Country",
            ylabel="Job Count",
            rotation=45,
            figsize=(8, 4.5),
        )
        if fig:
            st.pyplot(fig, use_container_width=True)
        else:
            st.info("No location data available.")

    with col_right:
        st.subheader("Remote Work Mix")
        remote_dist = df.groupBy("remote_ratio").count().orderBy("remote_ratio").toPandas()
        remote_dist["remote_label"] = remote_dist["remote_ratio"].map(
            {0: "Onsite", 50: "Hybrid", 100: "Fully Remote"}
        )
        fig = pie_chart(
            remote_dist,
            labels="remote_label",
            values="count",
            title="Remote vs Onsite",
        )
        if fig:
            st.pyplot(fig, use_container_width=True)
        else:
            st.info("No remote ratio data available.")

    st.divider()
    st.subheader("Quick Insights")
    st.write(
        "- Fully remote roles account for a meaningful share of the dataset.\n"
        "- Salary distribution is skewed toward mid-to-senior roles.\n"
        "- A small set of countries dominate hiring volume."
    )
