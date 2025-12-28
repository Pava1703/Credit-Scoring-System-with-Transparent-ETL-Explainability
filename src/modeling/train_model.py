import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import numpy as np


def train_model(df: pd.DataFrame, target_col: str):
    """
    Train a logistic regression model (safe for large datasets)
    """

    df = df.copy()

    # Separate features and target
    X = df.drop(columns=[target_col])
    y = df[target_col]

    # Keep only numeric columns
    X = X.select_dtypes(include=["int64", "float64"])

    # 🔑 VERY IMPORTANT: remove infinite values
    X.replace([np.inf, -np.inf], np.nan, inplace=True)

    # 🔑 VERY IMPORTANT: fill remaining NaNs
    X.fillna(0, inplace=True)

    # Train-test split
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # 🔑 Use solver suitable for large datasets
    model = LogisticRegression(
        max_iter=1000,
        solver="saga",
        n_jobs=-1
    )

    model.fit(X_train, y_train)

    print("Model training completed")

    return model, X_test, y_test
