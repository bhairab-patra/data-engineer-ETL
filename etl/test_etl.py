from extract import extract_employees, update_watermark
from tranform import transform_employees
from load import load_to_warehouse
from logger import get_logger
from validate_data import validate_data
logger = get_logger(__name__)

print("ETL Pipeline Start...")

df_raw, engine  = extract_employees()
if df_raw.empty:
    logger.info("No new data found — Pipeline skipped")
else:
    df_transform = transform_employees(df_raw)
    validate_data_frame = validate_data(df_transform)
    print(df_transform.columns.tolist())  
    print(df_transform)
    if validate_data_frame:
        print(f"validate_data_frame => {validate_data_frame}")
        df_load = load_to_warehouse(df_transform)
        update_watermark(engine)


logger.info("Pipeline Complete!")