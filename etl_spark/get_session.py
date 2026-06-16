"""
Creates and configures a SparkSession.
"""

from pyspark.sql import SparkSession
from etl.logger import get_logger
import os
from dotenv import load_dotenv
from sqlalchemy import create_engine


def get_spark_session():
    """
    Create and return a SparkSession.
    """
    spark = (
        SparkSession.builder.appName("Employee ETL")
        .config(
            "spark.jars",
            "file:///C:/JAVA_MS_2027/DATA_ENG/COMP_ETL/jars/postgresql-42.7.3.jar",
        )
        .getOrCreate()
    )
    return spark

