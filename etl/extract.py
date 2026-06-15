import pandas as pd
from sqlalchemy import create_engine, text
from logger import get_logger
from dotenv import load_dotenv
import os

load_dotenv()
SOURCE_DB = os.getenv("SOURCE_DB")
logger = get_logger(__name__)


def get_last_watermark(engine):
    """Aakhri baar kab data load hua"""
    with engine.connect() as conn:
        result = conn.execute(text("""
            SELECT last_loaded 
            FROM etl_watermark 
            WHERE table_name = 'employees'
        """))
        return result.scalar()

def update_watermark(engine):
    """Load hone ke baad timestamp update karo"""
    with engine.connect() as conn:
        conn.execute(text("""
            UPDATE etl_watermark 
            SET last_loaded = NOW()
            WHERE table_name = 'employees'
        """))
        conn.commit()
    logger.info("Watermark updated")


def extract_employees():

    try:
        engine = create_engine(SOURCE_DB)
        last_loaded = get_last_watermark(engine)
        print(f"last_loaded ================= {last_loaded}")
        
        query = text("""
            SELECT id, name, department, salary, join_date, updated_at
            FROM employees
            WHERE is_active = TRUE
            AND updated_at > :last_loaded
        """)
        
        df = pd.read_sql(query, engine, params={"last_loaded": last_loaded})
        logger.info(f"Extracted {len(df)} new/updated rows")
        return df, engine
    
    except Exception as e:
        logger.info(f"Extract failed: {e}")
        raise
