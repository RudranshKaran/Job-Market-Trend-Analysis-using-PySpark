from __future__ import annotations

import streamlit as st
from pyspark.sql import DataFrame, SparkSession
from pyspark.sql import functions as F

from app.components.charts import bar_chart, histogram
from app.components.layout import render_page_header
from app.components.metrics import render_metric_cards
from app.components.theme import apply_theme
from app.utils.app_state import get_spark, load_data_or_stop
from app.utils import analytics
from app.utils import sql_queries


REQUIRED_COLUMNS = ["salary_in_usd", "job_title", "experience_level", "company_location"]


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
        "Salary Analysis",
        "Explore salary distributions, top roles, and location-based pay trends.",
        "Compensation",
        ["Pay bands", "Top roles", "Distributions"],
    )

    if not _validate_columns(df):
        return

    avg_salary = df.select(F.avg("salary_in_usd").alias("avg_salary")).collect()[0][0] or 0
    max_salary = df.select(F.max("salary_in_usd").alias("max_salary")).collect()[0][0] or 0

    metrics = [
        {"label": "Average Salary", "value": f"${avg_salary:,.0f}", "subtitle": "USD"},
        {"label": "Top Salary", "value": f"${max_salary:,.0f}", "subtitle": "Highest role"},
    ]
    render_metric_cards(metrics)

    st.divider()
    col_left, col_right = st.columns([1.2, 1])

    with col_left:
        st.subheader("Top Paying Job Roles")
        top_roles = analytics.get_average_salary_by_role(df).orderBy(
            F.col("avg_salary_usd").desc()
        )
        top_roles_pd = top_roles.limit(10).toPandas()
        fig = bar_chart(
            top_roles_pd,
            x="job_title",
            y="avg_salary_usd",
            title="Top 10 Roles by Average Salary",
            xlabel="Job Title",
            ylabel="Avg Salary (USD)",
            rotation=45,
            figsize=(8, 4.5),
        )
        if fig:
            st.pyplot(fig, use_container_width=True)

    with col_right:
        st.subheader("Salary Distribution")
        salary_sample = df.select("salary_in_usd").dropna().limit(20000).toPandas()
        fig = histogram(
            salary_sample,
            column="salary_in_usd",
            title="Salary Distribution (Sample)",
            bins=30,
            xlabel="Salary (USD)",
        )
        if fig:
            st.pyplot(fig, use_container_width=True)

    st.divider()
    st.subheader("Salary by Experience Level")
    sql_view = sql_queries.create_temp_view(df)
    exp_salary = sql_queries.query_salary_by_experience_level(spark, view_name=sql_view).toPandas()
    exp_salary["experience_level"] = exp_salary["experience_level"].map(
        {"EN": "Entry-level", "MI": "Mid-level", "SE": "Senior-level", "EX": "Executive-level"}
    )
    fig = bar_chart(
        exp_salary,
        x="experience_level",
        y="avg_salary_usd",
        title="Average Salary by Experience Level",
        xlabel="Experience Level",
        ylabel="Avg Salary (USD)",
    )
    if fig:
        st.pyplot(fig, use_container_width=True)

    st.subheader("Salary by Country (Top 10)")
    salary_by_country = analytics.get_average_salary_by_country(df).orderBy(
        F.col("avg_salary_usd").desc()
    )
    country_pd = salary_by_country.limit(10).toPandas()
    fig = bar_chart(
        country_pd,
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

    with st.expander("Average Salary Table"):
        sql_avg = sql_queries.query_average_salary_by_role(spark, view_name=sql_view, limit=20)
        st.dataframe(sql_avg.toPandas(), use_container_width=True)

    st.divider()
    st.subheader("Insights")
    st.markdown(
        """
        <div class="insight-list">
        <ul>
            <li>Executive and senior roles show a clear salary premium.</li>
            <li>Salary distributions are right-skewed, indicating a long tail of high earners.</li>
            <li>A small number of countries consistently lead average salary benchmarks.</li>
        </ul>
        </div>
        """,
        unsafe_allow_html=True,
    )


render_page()
