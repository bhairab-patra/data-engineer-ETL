import pandas as pd
from sqlalchemy import create_engine, text
from datetime import date
from dotenv import load_dotenv
import os

load_dotenv()
WAREHOUSE_DB = os.getenv("WAREHOUSE_DB")


def load_to_warehouse(df: pd.DataFrame) -> pd.DataFrame:
    engine = create_engine(WAREHOUSE_DB)
    today = date.today()
    df["loaded_at"] = today

    # with engine.connect() as conn:
    #     conn.execute(
    #         text("DELETE FROM dept_salary_summary WHERE loaded_at = :today"),
    #         {"today": today},
    #     )
    #     conn.commit()

    df.to_sql(name="dept_salary_summary", con=engine, if_exists="append", index=False)

    return df
