# Job Market Trend Analysis using PySpark

## Project Overview
A modular PySpark backend with a Streamlit dashboard that analyzes job market trends from Kaggle's Data Science Job Salaries dataset. Phase 1 covers data ingestion, preprocessing, analytics, and Spark SQL queries. Phase 2 adds an interactive frontend for presentation-ready insights.

## Features
- Reusable Spark session utility
- CSV data loader with schema inference and preview
- Data preprocessing pipeline with cleaning and validation
- Analytics utilities for filtering, grouping, aggregation, and sorting
- Spark SQL query module with reusable analytics queries
- Streamlit dashboard with multi-page analytics
- KPI cards and presentation-ready visualizations

## Tech Stack
- Python 3.10+
- PySpark
- Spark SQL
- pandas
- matplotlib
- seaborn
- kagglehub
- Streamlit

## Folder Structure
```
app/
   main.py
   components/
      sidebar.py
      charts.py
      metrics.py
   pages/
      dashboard.py
      salary_analysis.py
      remote_work_analysis.py
      experience_analysis.py
      location_analysis.py
  utils/
    spark_session.py
    data_loader.py
    preprocess.py
    analytics.py
    sql_queries.py

data/
  raw/
  processed/

scripts/
  download_dataset.py
  run_preprocessing.py
  generate_insights.py

outputs/
  charts/
  reports/
  screenshots/

requirements.txt
README.md
.gitignore
```

## Setup Instructions
1. Create a virtual environment and install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Ensure Kaggle credentials are available for kagglehub. A common setup is to place your Kaggle API token at:
   - `~/.kaggle/kaggle.json` on Linux/macOS
   - `%USERPROFILE%\.kaggle\kaggle.json` on Windows

## How to Run
1. Download the dataset:
   ```bash
   python scripts/download_dataset.py
   ```
2. Run preprocessing to generate cleaned data:
   ```bash
   python scripts/run_preprocessing.py
   ```
3. Generate analytics insights:
   ```bash
   python scripts/generate_insights.py
   ```
4. Launch the Streamlit dashboard:
   ```bash
   streamlit run app/main.py
   ```

## Dataset Information
- Name: Data Science Job Salaries
- Source: Kaggle
- Link: https://www.kaggle.com/datasets/ruchi798/data-science-job-salaries

## Phase 1 Features
- Backend-only PySpark pipeline
- Modular utilities for reusable analytics
- Cleaned dataset output saved to `data/processed/cleaned_jobs` in parquet format

## Phase 2 Features
- Multi-page Streamlit dashboard
- Salary, remote work, experience, and location analysis pages
- KPI cards, charts, and insights for presentations

## Future Scope
- Advanced dashboard filters
- Automated report generation
- Advanced analytics and ML modeling
- Real-time data ingestion
