from __future__ import annotations

import argparse
import logging
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from app.utils.data_loader import load_csv_dataset
from app.utils.preprocess import preprocess_dataset
from app.utils.spark_session import get_spark_session


def _setup_logging() -> None:
    logging.basicConfig(
        level=logging.INFO,
        format="[%(levelname)s] %(message)s",
    )


def _parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run preprocessing pipeline.")
    parser.add_argument(
        "--input",
        type=str,
        default=str(Path("data") / "raw"),
        help="Path to CSV file or directory containing CSV.",
    )
    parser.add_argument(
        "--output-dir",
        type=str,
        default=str(Path("data") / "processed"),
        help="Output directory for processed data.",
    )
    parser.add_argument(
        "--app-name",
        type=str,
        default="Job Market Trend Analysis - Preprocessing",
        help="Spark application name.",
    )
    return parser.parse_args()


def main() -> None:
    _setup_logging()
    args = _parse_args()

    spark = get_spark_session(app_name=args.app_name)
    df = load_csv_dataset(spark, args.input)
    preprocess_dataset(df, args.output_dir)
    spark.stop()


if __name__ == "__main__":
    main()
