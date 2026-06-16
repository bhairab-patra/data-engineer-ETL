"""
Main ETL pipeline entry point.
"""

from etl_spark.extract import extract_employees
from etl_spark.get_session import get_spark_session
from etl_spark.transform import transform_employees
from etl_spark.load import load_to_warehouse
from etl.logger import get_logger

logger = get_logger(__name__)

spark = get_spark_session()

df_raw = extract_employees()

df_transform = transform_employees(df_raw)

print("Employee Data:")
df_transform.show()

load_to_warehouse(df_transform)

logger.info("Pipeline Complete!")
spark.stop()
