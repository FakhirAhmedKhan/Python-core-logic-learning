Day 3 with **Pandas** is the correct next step.

But do not start ML yet. Day 3 should focus on **reading, understanding, and simplifying data**.

## Day 3 Topic

```text
Pandas Basics + Real Dataset Reading
```

## What You Learn Today

```text
Pandas DataFrame
Read CSV / Excel file
head()
tail()
shape
columns
info()
describe()
select columns
filter rows
check missing values
rename columns
save cleaned file
```

## 1. Install Pandas

```bash
pip install pandas openpyxl xlrd
```

## 2. Import Pandas

```python
import pandas as pd
```

## 3. What is Pandas?

Pandas is used to work with **table data**.

Example:

```text
Excel file
CSV file
Database table
Sales data
Student marks data
Loan data
```

In Pandas, table data is called a **DataFrame**.

## 4. Read CSV File

```python
import pandas as pd

df = pd.read_csv("students.csv")

print(df)
```

## 5. Read Excel File

For `.xlsx`:

```python
df = pd.read_excel("student_loan_data.xlsx", engine="openpyxl")
```

For `.xls`:

```python
df = pd.read_excel("student_loan_data.xls", engine="xlrd")
```

## 6. Check First Rows

```python
print(df.head())
```

This shows first 5 rows.

## 7. Check Last Rows

```python
print(df.tail())
```

This shows last 5 rows.

## 8. Check Rows and Columns

```python
print(df.shape)
```

Example output:

```text
(3821, 25)
```

Meaning:

```text
3821 rows
25 columns
```

## 9. Check Column Names

```python
print(df.columns)
```

Better:

```python
print(df.columns.tolist())
```

## 10. Check Dataset Info

```python
print(df.info())
```

This tells:

```text
Column names
Data types
Missing values
Memory usage
```

## 11. Basic Summary

```python
print(df.describe())
```

This gives summary for numeric columns:

```text
count
mean
standard deviation
minimum
maximum
```

## 12. Select One Column

```python
print(df["school"])
```

## 13. Select Multiple Columns

```python
print(df[["school", "state", "school_type"]])
```

## 14. Filter Rows

Example: show only schools from Alaska:

```python
alaska_schools = df[df["state"] == "AK"]

print(alaska_schools)
```

## 15. Check Missing Values

```python
print(df.isnull().sum())
```

## 16. Rename Columns

```python
df = df.rename(columns={
    "School": "school",
    "State": "state",
    "School Type": "school_type"
})
```

## 17. Save Cleaned File

```python
df.to_csv("data.csv", index=False)
```

## Day 3 Practice Project

Build this:

```text
Student Loan Data Reader using Pandas
```

Features:

```text
Read Excel file
Fix header row
Remove extra first row
Rename columns
Check missing values
Show first 10 rows
Save cleaned CSV file
```

## Complete Day 3 Starter Code

```python
import pandas as pd
from pathlib import Path

file_path = Path("DataScienceDay2/student_loan_data.xls")

df = pd.read_excel(file_path, engine="xlrd", header=4)

df = df.iloc[1:].reset_index(drop=True)

df.columns = [
    "ope_id",
    "school",
    "state",
    "zip_code",
    "school_type",

    "subsidized_recipients",
    "subsidized_loans_originated_count",
    "subsidized_loans_originated_amount",
    "subsidized_disbursements_count",
    "subsidized_disbursements_amount",

    "unsubsidized_recipients",
    "unsubsidized_loans_originated_count",
    "unsubsidized_loans_originated_amount",
    "unsubsidized_disbursements_count",
    "unsubsidized_disbursements_amount",

    "parent_plus_recipients",
    "parent_plus_loans_originated_count",
    "parent_plus_loans_originated_amount",
    "parent_plus_disbursements_count",
    "parent_plus_disbursements_amount",

    "grad_plus_recipients",
    "grad_plus_loans_originated_count",
    "grad_plus_loans_originated_amount",
    "grad_plus_disbursements_count",
    "grad_plus_disbursements_amount",
]

print("First 5 Rows:")
print(df.head())

print("\nRows and Columns:")
print(df.shape)

print("\nColumn Names:")
print(df.columns.tolist())

print("\nMissing Values:")
print(df.isnull().sum())

df.to_csv("DataScienceDay2/data.csv", index=False)

print("\nCleaned file saved successfully.")
```

## Day 3 Final Goal

```text
Learn how to load real data, inspect it, clean the structure, and save a cleaner version.
```

Day 3 is not about deep analysis yet. It is about becoming comfortable with **Pandas DataFrame handling**.
