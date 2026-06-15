# ETL Project Setup Guide

## 1. Create Project Directory

```bash
mkdir etl_project
cd etl_project
```

## 2. Verify Python Installation

```bash
python --version

# or

python3 --version
```

## 3. Create Virtual Environment

```bash
python -m venv venv
```

## 4. Activate Virtual Environment

### Windows (Git Bash)

```bash
source venv/Scripts/activate
```

### Windows (Command Prompt)

```bash
venv\Scripts\activate
```

### Windows (PowerShell)

```powershell
.\venv\Scripts\Activate.ps1
```

## 5. Install Required Packages

```bash
pip install pandas sqlalchemy psycopg2-binary apache-airflow
```

Or install them separately:

```bash
pip install pandas sqlalchemy psycopg2-binary

pip install apache-airflow --constraint "https://raw.githubusercontent.com/apache/airflow/constraints-2.8.0/constraints-3.11.txt"

pip install apache-airflow-providers-standard
```

## 6. Verify Installed Packages

```bash
pip list
```

Expected packages:

* pandas
* SQLAlchemy
* psycopg2-binary
* apache-airflow

## 7. Create Project Structure

```bash
mkdir dags etl

touch etl/__init__.py
touch etl/extract.py
touch etl/transform.py
touch etl/load.py

touch dags/employee_etl_dag.py
```

## 8. Project Structure

```text
etl_project/
├── venv/
├── dags/
│   └── employee_etl_dag.py
└── etl/
    ├── __init__.py
    ├── extract.py
    ├── transform.py
    └── load.py
```

## 9. Generate Requirements File

```bash
pip freeze > requirements.txt
```

## 10. Install Dependencies from Requirements

```bash
pip install -r requirements.txt
```

## 11. Reinstall PostgreSQL Driver (If Needed)

```bash
pip install psycopg2-binary --force-reinstall
```

## 12. Verify Airflow Installation

Make sure the virtual environment is activated:

```bash
source venv/Scripts/activate
```

Check Airflow installation:

```bash
pip show apache-airflow
```

If Airflow is not installed:

```bash
pip install apache-airflow
```

Install standard providers:

```bash
pip install apache-airflow-providers-standard
```

## 13. Useful Commands

```bash
pip list
pip freeze > requirements.txt
pip install -r requirements.txt
pip show apache-airflow
```

## 14. ETL Components

### Extract Layer

* extract.py
* Reads employee data from source systems.

### Transform Layer

* transform.py
* Cleans and transforms raw data.

### Load Layer

* load.py
* Loads transformed data into the target warehouse.

### Airflow DAG

* employee_etl_dag.py
* Orchestrates the ETL workflow using Apache Airflow.
