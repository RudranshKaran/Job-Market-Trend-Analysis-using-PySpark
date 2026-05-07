# Job Market Trend Analysis using PySpark

## Project Overview
A modular PySpark backend with a Streamlit dashboard that analyzes job market trends from Kaggle's Data Science Job Salaries dataset. Phase 1 covers data ingestion, preprocessing, analytics, and Spark SQL queries. Phase 2 adds an interactive frontend for presentation-ready insights.

## Features
- Reusable Spark session utility
- CSV data loader with schema inference and preview
- Data preprocessing pipeline with cleaning and validation
- Analytics utilities for filtering, grouping, aggregation, and sorting
- Spark SQL query module with reusable analytics queries
- Streamlit dashboard with multi-page analytics (URL-based routing)
- KPI cards and presentation-ready visualizations
- Shared theme and page header components

## Tech Stack
- Python 3.10+
- PySpark
- Spark SQL
- pandas
- matplotlib
- seaborn
- kagglehub
- Streamlit
- setuptools (for PySpark on newer Python versions)

## Folder Structure
```
app/
   main.py
   components/
      sidebar.py
      charts.py
      metrics.py
      layout.py
      theme.py
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
    app_state.py

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

## Windows Notes
- PySpark is most stable with Java 17. If you see a `getSubject` security manager error, install JDK 17 and set `JAVA_HOME` accordingly.
- If you see errors about `winutils.exe`, `HADOOP_HOME`, or `NativeIO$Windows.access0`, complete the Hadoop setup steps below.

## Hadoop Setup (Windows)
Spark on Windows requires `winutils.exe` and `hadoop.dll` for local file operations.

1. Create a folder:
   ```text
   C:\hadoop\bin
   ```
2. Download the Hadoop Windows binaries that include:
   - `winutils.exe`
   - `hadoop.dll`

   Use a Hadoop 3.3.x build (3.3.6 or 3.3.5). Place both files in:
   ```text
   C:\hadoop\bin
   ```
3. Set environment variables:
   - `HADOOP_HOME = C:\hadoop`
   - Add `C:\hadoop\bin` to your system `PATH`
4. Open a new terminal and verify:
   ```powershell
   winutils.exe
   ```
5. Re-run preprocessing:
   ```bash
   python scripts/run_preprocessing.py
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
- Consistent hero-style headers across all pages

## Future Scope
- Advanced dashboard filters
- Automated report generation
- Advanced analytics and ML modeling
- Real-time data ingestion
