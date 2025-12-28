from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime


default_args = {
    "owner": "airflow",
    "start_date": datetime(2024, 1, 1),
    "retries": 1,
}

with DAG(
    dag_id="credit_scoring_pipeline",
    default_args=default_args,
    schedule_interval=None,
    catchup=False,
    description="End-to-end credit scoring data pipeline",
) as dag:

    # Task 1: Data ingestion
    data_ingestion = BashOperator(
        task_id="data_ingestion",
        bash_command="python src/data_ingestion/load_data.py",
    )

    # Task 2: Data cleaning and preprocessing
    data_cleaning = BashOperator(
        task_id="data_cleaning",
        bash_command="python src/data_cleaning/clean_data.py",
    )

    # Task 3: Feature engineering
    feature_engineering = BashOperator(
        task_id="feature_engineering",
        bash_command="python src/feature_engineering/feature_engineering.py",
    )

    # Task 4: Model training
    model_training = BashOperator(
        task_id="model_training",
        bash_command="python src/modeling/train_model.py",
    )

    # Task 5: Model evaluation
    model_evaluation = BashOperator(
        task_id="model_evaluation",
        bash_command="python src/evaluation/evaluate_model.py",
    )

    # Logical task dependencies
    data_ingestion >> data_cleaning >> feature_engineering >> model_training >> model_evaluation
