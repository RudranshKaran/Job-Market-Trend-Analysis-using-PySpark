from __future__ import annotations

import argparse
import logging
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from app.utils import analytics
from app.utils.spark_session import get_spark_session
from app.utils.sql_queries import (
    create_temp_view,
    query_average_salary_by_role,
    query_highest_paying_roles,
    query_remote_work_distribution,
    query_salary_by_country,
    query_salary_by_experience_level,
)


def _setup_logging() -> None:
    logging.basicConfig(
        level=logging.INFO,
        format="[%(levelname)s] %(message)s",
    )


def _parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Generate analytics insights.")
    parser.add_argument(
        "--input",
        type=str,
        default=str(Path("data") / "processed" / "cleaned_jobs"),
        help="Path to processed parquet directory.",
    )
    parser.add_argument(
        "--app-name",
        type=str,
        default="Job Market Trend Analysis - Insights",
        help="Spark application name.",
    )
    return parser.parse_args()


def main() -> None:
    _setup_logging()
    args = _parse_args()

    spark = get_spark_session(app_name=args.app_name)
    df = spark.read.parquet(args.input)

    logging.info("Filtering: fully remote jobs")
    analytics.get_remote_jobs(df).show(10, truncate=False)

    logging.info("Filtering: high salary jobs")
    analytics.get_high_salary_jobs(df).show(10, truncate=False)

    logging.info("Grouping: jobs by title")
    analytics.get_jobs_by_title(df).orderBy("count", ascending=False).show(10, truncate=False)

    logging.info("Aggregation: average salary by role")
    analytics.get_average_salary_by_role(df).orderBy("avg_salary_usd", ascending=False).show(10, truncate=False)

    logging.info("Sorting: most common job titles")
    analytics.get_most_common_job_titles(df).show(10, truncate=False)

    view_name = create_temp_view(df)

    logging.info("SQL: average salary by role")
    query_average_salary_by_role(spark, view_name=view_name).show(10, truncate=False)

    logging.info("SQL: highest paying roles")
    query_highest_paying_roles(spark, view_name=view_name).show(10, truncate=False)

    logging.info("SQL: remote work distribution")
    query_remote_work_distribution(spark, view_name=view_name).show(10, truncate=False)

    logging.info("SQL: salary by experience level")
    query_salary_by_experience_level(spark, view_name=view_name).show(10, truncate=False)

    logging.info("SQL: salary by country")
    query_salary_by_country(spark, view_name=view_name).show(10, truncate=False)

    spark.stop()


if __name__ == "__main__":
    main()
