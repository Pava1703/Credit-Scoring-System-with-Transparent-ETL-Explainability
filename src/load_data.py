import pandas as pd
from pathlib import Path

print("Starting data ingestion...")

data_path = Path("data/sample/loan.csv")

df = pd.read_csv(data_path)

print("Data loaded successfully")
print("Dataset shape:", df.shape)
print("First 5 rows:")
print(df.head())
