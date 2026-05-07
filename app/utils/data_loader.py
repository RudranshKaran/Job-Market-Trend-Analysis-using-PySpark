from __future__ import annotations

import logging
from pathlib import Path
from pyspark.sql import DataFrame, SparkSession

logger = logging.getLogger(__name__)


def _resolve_csv_path(input_path: Path) -> Path:
    if input_path.is_dir():
        csv_files = sorted(input_path.glob("*.csv"))
        if not csv_files:
            raise FileNotFoundError(f"No CSV files found in {input_path}")
        return csv_files[0]

    if input_path.is_file():
        return input_path

    raise FileNotFoundError(f"Input path not found: {input_path}")


def load_csv_dataset(spark: SparkSession, input_path: str | Path, preview_rows: int = 5) -> DataFrame:
    """Load a CSV dataset into a Spark DataFrame with schema inference."""
    csv_path = _resolve_csv_path(Path(input_path))
    logger.info("Loading CSV dataset: %s", csv_path)

    df = spark.read.csv(
        str(csv_path),
        header=True,
        inferSchema=True,
    )

    row_count = df.count()
    logger.info("Dataset loaded. Rows: %s, Columns: %s", row_count, len(df.columns))
    logger.info("Schema:")
    df.printSchema()

    logger.info("Preview (first %s rows):", preview_rows)
    df.show(preview_rows, truncate=False)

    return df
