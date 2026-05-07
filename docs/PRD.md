# Product Requirements Document (PRD)

# Project Title
## Job Market Trend Analysis using PySpark

---

# 1. Project Overview

The project aims to analyze trends in the data science job market using Big Data technologies, primarily Apache Spark (PySpark). The system will process job-related datasets to identify patterns related to salaries, job roles, employment types, company locations, remote work trends, and experience levels.

The project is being developed as part of the Big Data Technologies subject to provide hands-on experience in Big Data processing, data analytics, and distributed computing concepts using open-source tools.

---

# 2. Problem Statement

The modern job market generates massive amounts of recruitment and employment-related data through online job portals and professional platforms. Manually analyzing this data to identify meaningful hiring trends and salary insights is difficult and inefficient.

This project aims to solve this problem by leveraging PySpark to process and analyze job market datasets efficiently and generate meaningful insights regarding:

- Salary trends
- Job role demand
- Experience-based salary distribution
- Remote work adoption
- Company and location-based hiring patterns

---

# 3. Objectives

## Primary Objectives
- Implement Big Data processing using PySpark
- Perform data analysis on job market datasets
- Apply filtering, grouping, and aggregation operations
- Generate meaningful business insights from large datasets

## Secondary Objectives
- Implement Spark SQL queries
- Visualize trends using charts and graphs
- Understand distributed data processing concepts
- Build a structured analytics workflow using Big Data tools

---

# 4. Scope of the Project

The project focuses on analyzing structured job market datasets related to data science and AI-related roles.

## Included in Scope
- Dataset loading using PySpark
- Data cleaning and preprocessing
- DataFrame operations
- Aggregation and grouping
- Trend analysis
- Spark SQL queries
- Visualization and reporting

## Out of Scope
- Real-time streaming analytics
- Machine learning prediction models
- Deployment to production servers
- Web application/dashboard development

---

# 5. Dataset Information

## Dataset Name
Data Science Job Salaries Dataset

## Dataset Source
Kaggle

## Dataset Link
https://www.kaggle.com/datasets/ruchi798/data-science-job-salaries

## Dataset Description
The dataset contains information related to:
- Data science job roles
- Salary information
- Experience levels
- Employment types
- Remote work ratios
- Company locations
- Company sizes

---

# 6. Expected Dataset Columns

| Column Name | Description |
|---|---|
| work_year | Year of employment |
| experience_level | Employee experience level |
| employment_type | Full-time / Part-time / Contract |
| job_title | Name of the job role |
| salary | Salary amount |
| salary_currency | Currency used |
| salary_in_usd | Salary converted to USD |
| employee_residence | Employee country |
| remote_ratio | Percentage of remote work |
| company_location | Company location |
| company_size | Company size category |

---

# 7. Technologies & Tools

## Development Environment
- Google Colab

## Big Data Framework
- Apache Spark (PySpark)

## Dataset Platform
- Kaggle

## Programming Language
- Python

## Visualization Libraries
- Matplotlib
- Seaborn

## Optional Technologies
- Spark SQL
- Apache Hive (conceptual understanding)

## AI-Assisted Tools
- ChatGPT
- GitHub Copilot
- Cursor

---

# 8. System Architecture

```text
Kaggle Dataset
       ↓
Google Colab Environment
       ↓
PySpark Data Loading
       ↓
Data Cleaning & Preprocessing
       ↓
Filtering / Grouping / Aggregation
       ↓
Spark SQL Analysis
       ↓
Visualization & Insights
       ↓
Final Report & Presentation
````

---

# 9. Functional Requirements

## 9.1 Data Loading

* Load CSV dataset using PySpark
* Infer schema automatically
* Display initial dataset preview

## 9.2 Data Cleaning

* Remove null values
* Remove duplicate records
* Handle inconsistent values

## 9.3 Data Processing

The system must support:

* Filtering
* Grouping
* Aggregation
* Sorting

## 9.4 Spark SQL

* Create temporary SQL views
* Execute SQL queries on datasets

## 9.5 Visualization

Generate charts for:

* Salary trends
* Job distribution
* Experience-level analysis
* Remote work analysis

## 9.6 Insight Generation

The system should derive:

* Highest paying roles
* Most common job titles
* Remote work trends
* Country-wise salary patterns

---

# 10. Non-Functional Requirements

| Requirement     | Description                               |
| --------------- | ----------------------------------------- |
| Performance     | Efficient handling of large datasets      |
| Scalability     | Ability to process increasing data volume |
| Reliability     | Accurate processing and calculations      |
| Usability       | Easy-to-understand notebook structure     |
| Maintainability | Modular and readable code                 |

---

# 11. Project Phases

# Phase 1 — Data Processing & Big Data Operations

## Tasks

* Dataset collection
* Environment setup
* Data loading
* Data exploration
* Data cleaning
* Filtering
* Grouping
* Aggregation
* Sorting

## Deliverables

* Cleaned dataset
* Working PySpark notebook
* Processed data outputs

---

# Phase 2 — Trend Analysis & Reporting

## Tasks

* Trend analysis
* Spark SQL implementation
* Data visualization
* Insight generation
* Report preparation
* PPT preparation

## Deliverables

* Visualizations
* SQL query outputs
* Final insights
* Final report
* Presentation slides

---

# 12. Key Analyses to be Performed

## Salary Trend Analysis

* Average salary by role
* Highest paying job titles
* Salary distribution

## Experience Level Analysis

* Entry-level vs senior-level salaries
* Experience distribution

## Remote Work Analysis

* Percentage of remote jobs
* Remote work trends

## Location-Based Analysis

* Country-wise hiring trends
* Salary comparison across locations

## Employment Type Analysis

* Full-time vs contract roles
* Distribution of employment types

---

# 13. Sample PySpark Operations

## Filtering

```python
df.filter(df["remote_ratio"] == 100)
```

## Grouping

```python
df.groupBy("job_title").count()
```

## Aggregation

```python
df.groupBy("company_location").avg("salary_in_usd")
```

## Sorting

```python
df.orderBy("salary_in_usd", ascending=False)
```

---

# 14. Spark SQL Example

```sql
SELECT job_title,
AVG(salary_in_usd) AS avg_salary
FROM jobs
GROUP BY job_title
ORDER BY avg_salary DESC
```

---

# 15. Expected Outputs

The project should produce:

* Processed datasets
* Spark operation outputs
* Trend analysis reports
* Graphs and charts
* SQL query outputs
* Key insights
* Final presentation

---

# 16. Expected Insights

Possible insights include:

* Most in-demand data science roles
* Highest paying job positions
* Remote work growth trends
* Salary differences by experience level
* Country-wise salary comparisons

---

# 17. Deliverables

## Final Deliverables

* Google Colab Notebook
* PySpark Code
* Output Screenshots
* Final Report
* PPT Presentation

---

# 18. Team Responsibilities

| Team Member | Responsibility                        |
| ----------- | ------------------------------------- |
| Member 1    | Dataset collection & preprocessing    |
| Member 2    | PySpark implementation & Spark SQL    |
| Member 3    | Visualization, insights, report & PPT |

---

# 19. Future Scope

Possible future improvements:

* Real-time job market analysis
* Integration with live job APIs
* Machine learning salary prediction
* Interactive dashboards
* Streaming analytics using Spark Streaming

---

# 20. Conclusion

The project will provide practical exposure to Big Data technologies by implementing PySpark-based data processing and analytics on real-world job market datasets. The analysis will help identify meaningful trends in salaries, job roles, and remote work adoption while demonstrating core Big Data operations such as filtering, aggregation, grouping, and Spark SQL querying.