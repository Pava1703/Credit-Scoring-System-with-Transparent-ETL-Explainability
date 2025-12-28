import pandas as pd

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Perform basic data cleaning:
    - Remove duplicates
    - Handle missing values
    """

    df = df.copy()

    # Remove duplicate rows
    df.drop_duplicates(inplace=True)

    # Handle missing values (basic example)
    df.fillna(method="ffill", inplace=True)

    print("Data cleaning completed")
    print("Shape after cleaning:", df.shape)

    return df
