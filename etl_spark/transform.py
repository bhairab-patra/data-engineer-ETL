"""_summary_"""

from pyspark.sql import functions as F
from etl.logger import get_logger

logger = get_logger(__name__)


def transform_employees(df):
    """_summary_

    Args:
        df (_type_): _description_
    """
    logger.info("Transform started")

    df = df.filter(df.salary > 70000)

    df = df.na.drop(subset=["salary", "department"])

    # summary = df.groupBy("department").agg(
    #     F.count("id").alias("total_employees"),
    #     F.round(F.avg("salary"), 2).alias("avg_salary"),
    #     F.max("salary").alias("max_salary"),
    #     F.min("salary").alias("min_salary"),

    # )

    return df
