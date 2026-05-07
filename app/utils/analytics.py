from __future__ import annotations

from pyspark.sql import DataFrame
from pyspark.sql import functions as F


def get_remote_jobs(df: DataFrame) -> DataFrame:
    """Return fully remote jobs (remote_ratio = 100)."""
    return df.filter(F.col("remote_ratio") == 100)


def get_high_salary_jobs(df: DataFrame, threshold: int = 150000) -> DataFrame:
    """Return jobs with salary_in_usd greater than or equal to the threshold."""
    return df.filter(F.col("salary_in_usd") >= threshold)


def get_senior_level_jobs(df: DataFrame, levels: list[str] | None = None) -> DataFrame:
    """Return senior-level jobs based on experience levels (default: SE, EX)."""
    levels = levels or ["SE", "EX"]
    return df.filter(F.col("experience_level").isin(levels))


def get_full_time_jobs(df: DataFrame) -> DataFrame:
    """Return full-time jobs (employment_type = FT)."""
    return df.filter(F.col("employment_type") == "FT")


def get_jobs_by_title(df: DataFrame) -> DataFrame:
    """Count jobs grouped by title."""
    return df.groupBy("job_title").count()


def get_jobs_by_location(df: DataFrame) -> DataFrame:
    """Count jobs grouped by company location."""
    return df.groupBy("company_location").count()


def get_jobs_by_experience_level(df: DataFrame) -> DataFrame:
    """Count jobs grouped by experience level."""
    return df.groupBy("experience_level").count()


def get_jobs_by_employment_type(df: DataFrame) -> DataFrame:
    """Count jobs grouped by employment type."""
    return df.groupBy("employment_type").count()


def get_average_salary_by_role(df: DataFrame) -> DataFrame:
    """Compute average salary by job role."""
    return df.groupBy("job_title").agg(
        F.avg("salary_in_usd").alias("avg_salary_usd")
    )


def get_average_salary_by_country(df: DataFrame) -> DataFrame:
    """Compute average salary by company location."""
    return df.groupBy("company_location").agg(
        F.avg("salary_in_usd").alias("avg_salary_usd")
    )


def get_salary_extremes(df: DataFrame) -> DataFrame:
    """Return maximum and minimum salary_in_usd values."""
    return df.agg(
        F.max("salary_in_usd").alias("max_salary_usd"),
        F.min("salary_in_usd").alias("min_salary_usd"),
    )


def get_total_salary_by_country(df: DataFrame) -> DataFrame:
    """Compute total salary by company location."""
    return df.groupBy("company_location").agg(
        F.sum("salary_in_usd").alias("total_salary_usd")
    )


def get_highest_paying_jobs(df: DataFrame, limit: int = 20) -> DataFrame:
    """Return highest paying jobs by salary_in_usd."""
    return df.orderBy(F.col("salary_in_usd").desc()).limit(limit)


def get_most_common_job_titles(df: DataFrame, limit: int = 20) -> DataFrame:
    """Return most common job titles by count."""
    return df.groupBy("job_title").count().orderBy(F.col("count").desc()).limit(limit)


def get_top_hiring_locations(df: DataFrame, limit: int = 20) -> DataFrame:
    """Return top hiring locations by job count."""
    return df.groupBy("company_location").count().orderBy(F.col("count").desc()).limit(limit)
