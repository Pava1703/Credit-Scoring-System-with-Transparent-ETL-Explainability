import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent))

from src.data_ingestion.load_data import df
from src.data_cleaning.clean_data import clean_data
from src.feature_engineering.feature_engineering import engineer_features
from src.modeling.train_model import train_model
from src.evaluation.evaluate_model import evaluate_model

# Pipeline execution
df_clean = clean_data(df)
df_features = engineer_features(df_clean)

model, X_test, y_test = train_model(
    df_features,
    target_col="loan_status"   # change if needed
)

evaluate_model(model, X_test, y_test)
