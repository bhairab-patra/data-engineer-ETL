"""
Extract module for loading employee data from PostgreSQL.
"""

from pyspark.sql import SparkSession
from  etl.logger import get_logger
import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from etl_spark.get_session import get_spark_session


load_dotenv()
logger = get_logger(__name__)

SOURCE_DB =os.getenv('SOURCE_DB_SPARK')

DB_PROPERTIES = {
    "user":     "postgres",
    "password": os.getenv("DB_PASSWORD"),
    "driver":   "org.postgresql.Driver"
}

spark = get_spark_session()

def extract_employees():
    try:
        df = spark.read.jdbc(
            url = SOURCE_DB,
            table = "(SELECT id, name, department, salary, join_date FROM employees WHERE is_active = TRUE) AS emp",
            properties = DB_PROPERTIES
        )
        logger.info(f"Extracted {df.count()} rows")
        return df
    except Exception as e:
        logger.error(f"Extract failed: {e}")
        raise
        
 
    
