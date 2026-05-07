from __future__ import annotations

import streamlit as st
from pyspark.sql import functions as F

from app.components.charts import bar_chart
from app.components.metrics import render_metric_cards
from app.utils import analytics
from app.utils import sql_queries


REQUIRED_COLUMNS = ["company_location", "salary_in_usd"]


def _validate_columns(df) -> bool:
    missing = [col for col in REQUIRED_COLUMNS if col not in df.columns]
    if missing:
        st.error(f"Missing required columns: {', '.join(missing)}")
        return False
    return True


def render_page(df, spark) -> None:
    st.title("Location Analysis")
    st.caption("Identify top hiring countries and salary hotspots.")

    if not _validate_columns(df):
        return

    top_locations = analytics.get_top_hiring_locations(df, limit=10).toPandas()
    top_country = top_locations.iloc[0]["company_location"] if not top_locations.empty else "N/A"

    metrics = [
        {"label": "Top Hiring Country", "value": top_country, "subtitle": "Highest job volume"},
    ]
    render_metric_cards(metrics)

    st.divider()
    st.subheader("Top Hiring Countries")
    fig = bar_chart(
        top_locations,
        x="company_location",
        y="count",
        title="Top 10 Countries by Job Count",
        xlabel="Country",
        ylabel="Jobs",
        rotation=45,
        figsize=(8, 4.5),
    )
    if fig:
        st.pyplot(fig, use_container_width=True)

    st.subheader("Average Salary by Country")
    sql_view = sql_queries.create_temp_view(df)
    salary_by_country = sql_queries.query_salary_by_country(spark, view_name=sql_view, limit=10).toPandas()
    fig = bar_chart(
        salary_by_country,
        x="company_location",
        y="avg_salary_usd",
        title="Top 10 Countries by Avg Salary",
        xlabel="Country",
        ylabel="Avg Salary (USD)",
        rotation=45,
        figsize=(8, 4.5),
    )
    if fig:
        st.pyplot(fig, use_container_width=True)

    st.divider()
    st.subheader("Insights")
    st.write(
        "- Hiring volume is concentrated in a small group of countries.\n"
        "- Salary leaders are not always the highest-volume locations.\n"
        "- Location continues to be a key factor in compensation bands."
    )
