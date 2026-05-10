import pandas as pd
from pathlib import Path

file_path = Path("DataScienceDay3/student_loan_data.xls")

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

df.to_csv("DataScienceDay2/cleaned_student_loan_data.csv", index=False)

print("\nCleaned file saved successfully.")