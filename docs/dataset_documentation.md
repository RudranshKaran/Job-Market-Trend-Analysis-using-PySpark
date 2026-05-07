# Dataset Documentation

# Project Title
## Job Market Trend Analysis using PySpark

---

# 1. Dataset Overview

This project uses the **Data Science Job Salaries** dataset to analyze trends in the global data science job market using PySpark and Big Data analytics techniques.

The dataset contains information related to:
- Job roles
- Salaries
- Experience levels
- Employment types
- Remote work ratios
- Company locations
- Company sizes

The dataset is structured and suitable for performing Big Data operations such as filtering, grouping, aggregation, sorting, and Spark SQL analysis.

---

# 2. Dataset Source

## Platform
Kaggle

## Dataset Name
Data Science Job Salaries

## Dataset Author
Ruchi798

## Dataset Link
https://www.kaggle.com/datasets/ruchi798/data-science-job-salaries

---

# 3. Dataset Acquisition

The dataset is downloaded using the `kagglehub` library.

## Dataset Download Code

```python id="n0ww4q"
import kagglehub

# Download latest version
path = kagglehub.dataset_download("ruchi798/data-science-job-salaries")

print("Path to dataset files:", path)
````

---

# 4. Dataset Purpose

The dataset is used to:

* Analyze salary trends in data science jobs
* Identify high-paying job roles
* Study remote work adoption
* Compare salaries across countries
* Analyze experience-based salary distribution
* Perform Big Data processing using PySpark

---

# 5. Dataset Characteristics

| Attribute            | Details                   |
| -------------------- | ------------------------- |
| Dataset Type         | Structured CSV Dataset    |
| Domain               | Job Market / Data Science |
| Data Format          | CSV                       |
| Source Platform      | Kaggle                    |
| Suitable For         | Big Data Analytics        |
| Processing Framework | PySpark                   |

---

# 6. Dataset Features / Columns

| Column Name        | Description                       |
| ------------------ | --------------------------------- |
| work_year          | Year in which the salary was paid |
| experience_level   | Experience level of employee      |
| employment_type    | Type of employment (FT/PT/CT/FL)  |
| job_title          | Job role/title                    |
| salary             | Original salary amount            |
| salary_currency    | Currency of salary                |
| salary_in_usd      | Salary converted to USD           |
| employee_residence | Employee residence country        |
| remote_ratio       | Percentage of remote work         |
| company_location   | Company location                  |
| company_size       | Company size category             |

---

# 7. Column Details

## 7.1 work_year

Represents the year in which the salary was paid.

### Example Values

* 2020
* 2021
* 2022

---

## 7.2 experience_level

Represents the seniority level of employees.

| Code | Meaning         |
| ---- | --------------- |
| EN   | Entry-level     |
| MI   | Mid-level       |
| SE   | Senior-level    |
| EX   | Executive-level |

---

## 7.3 employment_type

Represents the type of employment.

| Code | Meaning   |
| ---- | --------- |
| FT   | Full-time |
| PT   | Part-time |
| CT   | Contract  |
| FL   | Freelance |

---

## 7.4 job_title

Represents the job role.

### Example Roles

* Data Scientist
* Machine Learning Engineer
* Data Analyst
* AI Engineer

---

## 7.5 salary

Original salary amount before currency conversion.

---

## 7.6 salary_currency

Currency in which salary is paid.

### Example Values

* USD
* EUR
* INR

---

## 7.7 salary_in_usd

Salary converted into USD for standard comparison and analysis.

---

## 7.8 employee_residence

Country where the employee resides.

---

## 7.9 remote_ratio

Indicates the percentage of remote work.

| Value | Meaning          |
| ----- | ---------------- |
| 0     | No remote work   |
| 50    | Partially remote |
| 100   | Fully remote     |

---

## 7.10 company_location

Country where the company is located.

---

## 7.11 company_size

Represents company size.

| Code | Meaning |
| ---- | ------- |
| S    | Small   |
| M    | Medium  |
| L    | Large   |

---

# 8. Dataset Loading using PySpark

The dataset will be loaded into a PySpark DataFrame for distributed data processing.

## Sample Code

```python id="y2x5hq"
from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("Job Market Trend Analysis") \
    .getOrCreate()

df = spark.read.csv(
    "/content/data_science_job_salaries.csv",
    header=True,
    inferSchema=True
)

df.show()
```

---

# 9. Initial Dataset Exploration

The following operations will be performed to understand the dataset structure.

## Schema Inspection

```python id="j0kwzd"
df.printSchema()
```

---

## Display Sample Rows

```python id="msm7ak"
df.show(5)
```

---

## Statistical Summary

```python id="clj8p0"
df.describe().show()
```

---

# 10. Data Preprocessing Plan

The dataset may contain:

* Null values
* Duplicate records
* Inconsistent formatting

The following preprocessing steps will be applied:

## Planned Operations

* Remove null values
* Remove duplicates
* Validate salary fields
* Standardize categorical values

---

# 11. Expected Dataset Usage

The dataset will be used for:

| Analysis Type        | Purpose                        |
| -------------------- | ------------------------------ |
| Salary Analysis      | Identify high-paying roles     |
| Experience Analysis  | Compare salaries by experience |
| Remote Work Analysis | Study work-from-home trends    |
| Location Analysis    | Analyze country-wise hiring    |
| Employment Analysis  | Compare employment types       |

---

# 12. Big Data Operations Planned

The project will implement the following PySpark operations on the dataset:

## Filtering

Example:

```python id="1qh9o4"
df.filter(df["remote_ratio"] == 100)
```

---

## Grouping

Example:

```python id="r4g8m6"
df.groupBy("job_title").count()
```

---

## Aggregation

Example:

```python id="u93m07"
df.groupBy("company_location").avg("salary_in_usd")
```

---

## Sorting

Example:

```python id="38y4jk"
df.orderBy("salary_in_usd", ascending=False)
```

---

# 13. Spark SQL Usage

The dataset will also be queried using Spark SQL.

## Example Query

```sql id="ikozc2"
SELECT job_title,
AVG(salary_in_usd) AS average_salary
FROM jobs
GROUP BY job_title
ORDER BY average_salary DESC
```

---

# 14. Expected Insights from Dataset

The dataset is expected to help derive insights such as:

* Highest paying job roles
* Most common employment types
* Salary distribution across countries
* Remote work adoption trends
* Experience-level salary comparison

---

# 15. Conclusion

The selected Kaggle dataset provides structured and analysis-ready information related to data science job salaries and employment trends. Its well-organized format makes it highly suitable for implementing Big Data analytics using PySpark and Spark SQL while generating meaningful insights related to the modern job market.