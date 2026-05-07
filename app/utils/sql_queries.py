from __future__ import annotations

from pyspark.sql import DataFrame, SparkSession


def create_temp_view(df: DataFrame, view_name: str = "jobs") -> str:
    """Create or replace a temporary SQL view."""
    df.createOrReplaceTempView(view_name)
    return view_name


def query_average_salary_by_role(
    spark: SparkSession, view_name: str = "jobs", limit: int = 20
) -> DataFrame:
    query = f"""
    SELECT
        job_title,
        AVG(salary_in_usd) AS avg_salary_usd
    FROM {view_name}
    GROUP BY job_title
    ORDER BY avg_salary_usd DESC
    """
    if limit:
        query += f"\n    LIMIT {limit}"
    return spark.sql(query)


def query_highest_paying_roles(
    spark: SparkSession, view_name: str = "jobs", limit: int = 20
) -> DataFrame:
    query = f"""
    SELECT
        job_title,
        MAX(salary_in_usd) AS max_salary_usd
    FROM {view_name}
    GROUP BY job_title
    ORDER BY max_salary_usd DESC
    """
    if limit:
        query += f"\n    LIMIT {limit}"
    return spark.sql(query)


def query_remote_work_distribution(
    spark: SparkSession, view_name: str = "jobs"
) -> DataFrame:
    query = f"""
    SELECT
        remote_ratio,
        COUNT(*) AS total_jobs
    FROM {view_name}
    GROUP BY remote_ratio
    ORDER BY remote_ratio
    """
    return spark.sql(query)


def query_salary_by_experience_level(
    spark: SparkSession, view_name: str = "jobs"
) -> DataFrame:
    query = f"""
    SELECT
        experience_level,
        AVG(salary_in_usd) AS avg_salary_usd
    FROM {view_name}
    GROUP BY experience_level
    ORDER BY avg_salary_usd DESC
    """
    return spark.sql(query)


def query_salary_by_country(
    spark: SparkSession, view_name: str = "jobs", limit: int = 20
) -> DataFrame:
    query = f"""
    SELECT
        company_location,
        AVG(salary_in_usd) AS avg_salary_usd
    FROM {view_name}
    GROUP BY company_location
    ORDER BY avg_salary_usd DESC
    """
    if limit:
        query += f"\n    LIMIT {limit}"
    return spark.sql(query)
