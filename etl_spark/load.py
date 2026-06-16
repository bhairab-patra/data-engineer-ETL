from etl.logger import get_logger
import os
from dotenv import load_dotenv

load_dotenv()
logger = get_logger(__name__)

WAREHOUSE_URL = "jdbc:postgresql://localhost:5432/warehouse_db"


DB_PROPERTIES = {
    "user": "postgres",
    "password": os.getenv("DB_PASSWORD"),
    "driver": "org.postgresql.Driver",
}


def load_to_warehouse(df):
    """_summary_

    Args:
        df (_type_): _description_
    """
    try:
        df.write.jdbc(
            url=WAREHOUSE_URL,
            table="salary_summary_spark",
            mode="append",  # Pandas: if_exists='append'
            properties=DB_PROPERTIES,
        )
        logger.info(f"Loaded {df.count()} rows to warehouse")
    except Exception as e:
        logger.info(f"Load failed: {e}")
        raise
