from __future__ import annotations

import streamlit as st
from pyspark.sql import functions as F

from app.components.charts import bar_chart
from app.components.metrics import render_metric_cards
from app.utils import analytics
from app.utils import sql_queries


REQUIRED_COLUMNS = ["experience_level", "salary_in_usd"]


def _validate_columns(df) -> bool:
    missing = [col for col in REQUIRED_COLUMNS if col not in df.columns]
    if missing:
        st.error(f"Missing required columns: {', '.join(missing)}")
        return False
    return True


def _label_experience(level: str) -> str:
    labels = {
        "EN": "Entry-level",
        "MI": "Mid-level",
        "SE": "Senior-level",
        "EX": "Executive-level",
    }
    return labels.get(level, level)


def render_page(df, spark) -> None:
    st.title("Experience Analysis")
    st.caption("Compare job volume and salaries across experience levels.")

    if not _validate_columns(df):
        return

    exp_counts = analytics.get_jobs_by_experience_level(df).orderBy("count", ascending=False)
    exp_pd = exp_counts.toPandas()
    exp_pd["experience_level"] = exp_pd["experience_level"].map(_label_experience)

    highest_exp = exp_pd.iloc[0]["experience_level"] if not exp_pd.empty else "N/A"

    metrics = [
        {"label": "Top Experience Tier", "value": highest_exp, "subtitle": "Most common level"},
    ]
    render_metric_cards(metrics)

    st.divider()
    st.subheader("Experience Level Distribution")
    fig = bar_chart(
        exp_pd,
        x="experience_level",
        y="count",
        title="Job Count by Experience Level",
        xlabel="Experience",
        ylabel="Job Count",
    )
    if fig:
        st.pyplot(fig, use_container_width=True)

    st.subheader("Salary by Experience Level")
    sql_view = sql_queries.create_temp_view(df)
    exp_salary = sql_queries.query_salary_by_experience_level(spark, view_name=sql_view).toPandas()
    exp_salary["experience_level"] = exp_salary["experience_level"].map(_label_experience)
    fig = bar_chart(
        exp_salary,
        x="experience_level",
        y="avg_salary_usd",
        title="Average Salary by Experience Level",
        xlabel="Experience",
        ylabel="Avg Salary (USD)",
    )
    if fig:
        st.pyplot(fig, use_container_width=True)

    st.divider()
    st.subheader("Insights")
    st.write(
        "- Senior and executive roles command the strongest salary bands.\n"
        "- Entry-level roles dominate volume but trail in compensation.\n"
        "- Experience level is one of the strongest predictors of pay."
    )
