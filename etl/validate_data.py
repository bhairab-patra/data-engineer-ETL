def validate_data(df):
    # Check 1 — Empty dataframe
    if df.empty:
        raise ValueError("No data to validate!")

    # Check 2 — Required columns hain?
    required = [
        "department",
        "total_employees",
        "avg_salary",
        "max_salary",
        "min_salary",
        "avg_experience",
    ]
    missing = [c for c in required if c not in df.columns]
    if missing:
        raise ValueError(f"Missing columns: {missing}")

    # Check 3 — avg_salary negative toh nahi?
    if (df["avg_salary"] < 0).any():
        raise ValueError("Negative salary found!")

    # Check 4 — total_employees zero toh nahi?
    if (df["total_employees"] == 0).any():
        raise ValueError("Department with zero employees found!")

    return True


# Industry level:
#  →   Row count threshold
#   →   Data type validation
#      →   Outlier detection
#    →   Null percentage check
#   →   Duplicate detection
#   →   Referential integrity
