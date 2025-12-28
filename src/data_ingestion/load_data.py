import pandas as pd
from pathlib import Path

print("Starting data ingestion...")

data_path = Path("data/sample/loan.csv")

df = pd.read_csv(data_path, nrows=200000)


print("Data loaded successfully")
print("Dataset shape:", df.shape)
