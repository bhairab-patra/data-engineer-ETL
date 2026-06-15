import pandas as pd
from sqlalchemy import create_engine, text
from logger import get_logger
from dotenv import load_dotenv
import os

load_dotenv()
SOURCE_DB = os.getenv("SOURCE_DB")
logger = get_logger(__name__)

def get_engine():
    return create_engine(SOURCE_DB)

def get_last_watermark(engine, table_name):
    """Aakhri baar kab data load hua"""
    with engine.connect() as conn:
        result = conn.execute(text("""
            SELECT last_loaded 
            FROM etl_watermark 
            WHERE table_name = table_name
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
        engine = get_engine()
        last_loaded = get_last_watermark(engine, 'employees')
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

def extract_departments():
    try:
        engine = get_engine()
        last_loaded = get_last_watermark(engine, 'departments')
        print(f"last_loaded ================= {last_loaded}")
        
        query = text("""
            SELECT dept_id, dept_name, location, budget, updated_at
            FROM departments
            WHERE updated_at > :last_loaded
        """)
        
        df = pd.read_sql(query, engine, params={"last_loaded": last_loaded})
        
        logger.info(f"Extracted {len(df)} new/updated rows")
        return df, engine
    
    except Exception as e:
        logger.info(f"Extract failed: {e}")
        raise