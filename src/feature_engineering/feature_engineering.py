import pandas as pd


def engineer_features(df: pd.DataFrame) -> pd.DataFrame:
    """
    Create engineered features for loan default prediction
    """

    df = df.copy()

    # ---- Income related features ----
    if "annual_inc" in df.columns:
        df["monthly_income"] = df["annual_inc"] / 12

    # ---- Debt related features ----
    if "dti" in df.columns and "monthly_income" in df.columns:
        df["estimated_monthly_debt"] = (
            df["monthly_income"] * df["dti"] / 100
        )

    # ---- Employment length encoding (ordinal) ----
    if "emp_length" in df.columns:
        emp_map = {
            "< 1 year": 0,
            "1 year": 1,
            "2 years": 2,
            "3 years": 3,
            "4 years": 4,
            "5 years": 5,
            "6 years": 6,
            "7 years": 7,
            "8 years": 8,
            "9 years": 9,
            "10+ years": 10
        }
        df["emp_length_num"] = df["emp_length"].map(emp_map)

    print("Feature engineering completed")
    print("Shape after feature engineering:", df.shape)

    return df
