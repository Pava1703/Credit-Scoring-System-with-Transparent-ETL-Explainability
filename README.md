# Credit Scoring System – End-to-End Data & ML Pipeline

This project implements a complete end-to-end **credit scoring data pipeline** using Python and Apache Airflow.  
The pipeline covers data ingestion, cleaning, feature engineering, machine learning modeling, and evaluation, with all outputs generated automatically from code.


##Project Overview

The objective of this project is to build a reproducible data pipeline for **credit risk analysis**.

The pipeline:
- Ingests loan data
- Performs data cleaning and preprocessing
- Applies feature engineering
- Trains a simple machine learning model
- Evaluates model performance using standard metrics and visualizations

Apache Airflow is used to **orchestrate the pipeline stages conceptually** via a Directed Acyclic Graph (DAG).

## Dataset

The original dataset is **not included in this repository** due to GitHub file size limits (>100 MB).

Dataset source:
  Lending Club Loan Data (2007–2015): 
  https://www.kaggle.com/datasets/adarshsng/lending-club-loan-data-csv Kaggle

A sampled subset was used locally for development and testing.

## Research Questions

This project is motivated by the following research questions, as defined in the project proposal:

**RQ1:**  
 In a credit-scoring pipeline built on the Lending Club dataset, how does providing 
systematic, step-by-step documentation and visualization of every ETL and feature
engineering transformation affect borrowers’ perceived understandability and trustworthiness 
of SHAP-based rejection explanations?

**RQ2:**  
To what extent can a fully documented and visualised transparent ETL pipeline serve 
as a governance mechanism that improves regulatory compliance and stakeholder trust in 
Scikit-learn-based credit scoring models using the Lending Club dataset?

**RQ3:**  
Can the systematic documentation of ETL provenance and its integration with basic 
SHAP explanations generate consumer-friendly, legally compliant rejection letters for high
risk Lending Club loans, and how do borrowers rate their clarity and fairness compared to 
standard reason codes?


## Project Structure

```text
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
```



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

## How to Run the Code

Create and activate a virtual environment
Install dependencies:
   ```bash
   pip install -r requirements.txt

Run the full end-to-end pipeline:
   python test_pipe.py

---

## Airflow DAG

An Apache Airflow DAG is provided to orchestrate the complete pipeline.

- **DAG file:** `dags/credit_scoring_pipeline_dag.py`
- The DAG contains **multiple meaningful tasks**, each representing a pipeline stage:
  - Data ingestion
  - Data cleaning
  - Feature engineering
  - Model training
  - Model evaluation
- Logical dependencies are defined between tasks to reflect the correct execution order.

## DAG Execution (Conceptual)

The DAG is **runnable locally in a conceptual sense**, meaning:
- It is valid Airflow syntax
- It uses real Airflow operators (`BashOperator`)
- It executes local Python scripts
- It correctly represents the pipeline stages and dependencies

Actual execution requires a compatible Apache Airflow environment and is outside the scope of this assignment.

## How to Run the Airflow Dag

Copy the DAG file into your local Airflow dags/ directory:

dags/credit_scoring_pipeline_dag.py

Start Airflow services:

airflow webserver
airflow scheduler

Open the Airflow UI:

http://localhost:8080
Enable and trigger the DAG:

credit_scoring_pipeline_dag

---

## Reproducibility

- All figures and tables are generated directly from code
- No manual creation of outputs is performed
- Outputs are saved automatically to the `figures/` and `tables/` directories

---

## Folder Structure Explanation

- **dags/**  
  Contains the Apache Airflow DAG definition.  
  The DAG represents the complete credit scoring pipeline and defines the logical task dependencies between data ingestion, cleaning, feature engineering, modeling, and evaluation stages.

- **src/**  
  Contains all core pipeline logic, implemented in a modular manner:
  
  - **data_ingestion/**  
    Handles loading of raw loan data from CSV files into Pandas DataFrames.
  
  - **data_cleaning/**  
    Performs preprocessing steps such as missing value handling, type correction, and basic data validation.
  
  - **feature_engineering/**  
    Creates derived features required for machine learning, including transformations and feature selection.
  
  - **modeling/**  
    Trains a simple Scikit-learn based machine learning model for credit risk prediction.
  
  - **evaluation/**  
    Evaluates model performance using standard classification metrics and generates visualizations and summary tables.

- **data/**  
  Directory reserved for datasets.  
  The original dataset is not included in the repository due to size constraints, but the structure is maintained for reproducibility.

- **figures/**  
  Stores all automatically generated plots, such as the confusion matrix and ROC curve.

- **tables/**  
  Stores automatically generated tabular outputs, such as the classification report.

- **test_pipe.py**  
  A script to execute the complete end-to-end pipeline sequentially without Airflow.

- **requirements.txt**  
  Lists all Python dependencies required to run the pipeline.

- **README.md**  
  Project documentation, including setup instructions, research questions, and pipeline explanation.

