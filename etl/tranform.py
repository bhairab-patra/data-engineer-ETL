import pandas as pd
from datetime import date


def transform_employees(df: pd.DataFrame) -> pd.DataFrame:

    # i Remove Nulls
    df = df.dropna(subset=["salary", "department"])

    # Salary Should not Negative

    df = df[df["salary"] > 0]

    today = date.today()
    df["join_date"] = pd.to_datetime(df["join_date"])
    df["experience_years"] = (
        (pd.Timestamp(date.today()) - df["join_date"]).dt.days // 365
    ).astype(int)

    # Step 4 — Department wise summary banao
    summary = (
        df.groupby("department")
        .agg(
            total_employees=("id", "count"),
            avg_salary=("salary", "mean"),
            max_salary=("salary", "max"),
            min_salary=("salary", "min"),
            avg_experience=("experience_years", "mean"),
        )
        .reset_index()
    )

    # Step 5 — Round karo
    summary["avg_salary"] = summary["avg_salary"].round(2)
    summary["avg_experience"] = summary["avg_experience"].round(1)

   
    return summary  # sirf 4 rows — ek per department
