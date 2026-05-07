from __future__ import annotations

import logging
from pathlib import Path
from pyspark.sql import DataFrame
from pyspark.sql import functions as F

logger = logging.getLogger(__name__)


def drop_nulls(df: DataFrame) -> DataFrame:
    """Remove rows with any null values."""
    return df.dropna()


def drop_duplicates(df: DataFrame) -> DataFrame:
    """Remove duplicate rows."""
    return df.dropDuplicates()


def validate_salary_columns(df: DataFrame, min_salary: int = 1) -> DataFrame:
    """Filter rows with invalid salary values if salary columns exist."""
    conditions = []
    if "salary" in df.columns:
        conditions.append(F.col("salary") >= min_salary)
    if "salary_in_usd" in df.columns:
        conditions.append(F.col("salary_in_usd") >= min_salary)

    if not conditions:
        return df

    combined = conditions[0]
    for cond in conditions[1:]:
        combined = combined & cond

    return df.filter(combined)


def standardize_categorical_values(df: DataFrame) -> DataFrame:
    """Standardize selected categorical columns for consistent analysis."""
    standardized = df

    upper_cols = ["experience_level", "employment_type", "company_size"]
    for col_name in upper_cols:
        if col_name in standardized.columns:
            standardized = standardized.withColumn(
                col_name, F.upper(F.trim(F.col(col_name)))
            )

    trim_cols = ["job_title", "company_location", "employee_residence"]
    for col_name in trim_cols:
        if col_name in standardized.columns:
            standardized = standardized.withColumn(
                col_name, F.trim(F.col(col_name))
            )

    return standardized


def preprocess_dataset(
    df: DataFrame,
    output_dir: str | Path,
    output_name: str = "cleaned_jobs",
) -> DataFrame:
    """Run preprocessing steps and persist the cleaned dataset to disk."""
    before_count = df.count()
    logger.info("Starting preprocessing. Rows before cleaning: %s", before_count)

    cleaned = drop_nulls(df)
    cleaned = drop_duplicates(cleaned)
    cleaned = validate_salary_columns(cleaned)
    cleaned = standardize_categorical_values(cleaned)

    after_count = cleaned.count()
    removed = before_count - after_count
    logger.info("Rows after cleaning: %s", after_count)
    logger.info("Rows removed during cleaning: %s", removed)

    output_path = Path(output_dir) / output_name
    output_path.mkdir(parents=True, exist_ok=True)

    cleaned.write.mode("overwrite").parquet(str(output_path))
    logger.info("Cleaned dataset saved to: %s", output_path)

    return cleaned
