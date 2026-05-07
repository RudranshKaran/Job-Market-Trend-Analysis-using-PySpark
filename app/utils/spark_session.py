import logging
from pyspark.sql import SparkSession


def get_spark_session(app_name: str = "Job Market Trend Analysis", master: str | None = None) -> SparkSession:
    """Create and return a reusable SparkSession."""
    builder = SparkSession.builder.appName(app_name)
    if master:
        builder = builder.master(master)

    spark = builder.getOrCreate()
    logging.getLogger(__name__).info("Spark session started: %s", app_name)
    return spark
