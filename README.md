# Credit Scoring System – End-to-End Data & ML Pipeline

This project implements a complete end-to-end **credit scoring data pipeline** using Python and Apache Airflow.  
The pipeline covers data ingestion, cleaning, feature engineering, machine learning modeling, and evaluation, with all outputs generated automatically from code.

---

## Project Overview

The objective of this project is to build a reproducible data pipeline for credit risk analysis.  
The pipeline processes loan data, applies preprocessing and feature engineering, trains a simple machine learning model, and evaluates its performance using standard metrics and visualizations.

Apache Airflow is used to **orchestrate the pipeline stages conceptually** via a Directed Acyclic Graph (DAG).

---

## Project Structure

Credit Scoring System/
├── dags/
│ └── credit_scoring_pipeline_dag.py
├── src/
│ ├── data_ingestion/
│ │ └── load_data.py
│ ├── data_cleaning/
│ │ └── clean_data.py
│ ├── feature_engineering/
│ │ └── feature_engineering.py
│ ├── modeling/
│ │ └── train_model.py
│ └── evaluation/
│ └── evaluate_model.py
├── data/
│ └── sample/
│ └── loan.csv
├── figures/
│ ├── confusion_matrix.pdf
│ └── roc_curve.pdf
├── tables/
│ └── classification_report.csv
├── test_pipe.py
├── requirements.txt
└── README.md


---

## Data Pipeline Stages

### 1. Data Ingestion
- Loads loan data from a CSV file
- Uses a sampled subset of the dataset for efficient local execution

### 2. Data Cleaning & Preprocessing
- Handles missing values
- Ensures numerical stability and consistency

### 3. Transformation & Feature Engineering
- Encodes categorical variables
- Creates derived numerical features relevant to credit risk

### 4. Analytical / ML Modeling
- Trains a Logistic Regression model
- Handles large datasets and convergence constraints

### 5. Evaluation
- Generates a classification report
- Produces a confusion matrix
- Generates a ROC curve (binary default vs non-default)
- Saves all outputs automatically as CSV and PDF files

---

## Airflow DAG (Pipeline Orchestration)

An Apache Airflow DAG is provided to orchestrate the complete pipeline.

- **DAG file:** `dags/credit_scoring_pipeline_dag.py`
- The DAG contains **multiple meaningful tasks**, each representing a pipeline stage:
  - Data ingestion
  - Data cleaning
  - Feature engineering
  - Model training
  - Model evaluation
- Logical dependencies are defined between tasks to reflect the correct execution order.

### DAG Execution (Conceptual)

The DAG is **runnable locally in a conceptual sense**, meaning:
- It is valid Airflow syntax
- It uses real Airflow operators (`BashOperator`)
- It executes local Python scripts
- It correctly represents the pipeline stages and dependencies

Actual execution requires a compatible Apache Airflow environment and is outside the scope of this assignment.

---

## Reproducibility

- All figures and tables are generated directly from code
- No manual creation of outputs is performed
- Outputs are saved automatically to the `figures/` and `tables/` directories

---

## How to Run the Pipeline

### Install dependencies
```bash
pip install -r requirements.txt
