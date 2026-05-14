import pandas as pd
from pathlib import Path

<<<<<<< HEAD
file_path = Path("DataScienceDay3/data.csv")
=======
file_path = Path("DataScienceDay3/cleaned_student_loan_data.csv")
>>>>>>> b816be63cf4526c1ae2e270e1859b9a9577762ca

df = pd.read_csv(file_path)

print("First 5 Rows:")
print(df.head())

print("\nRows and Columns:")
print(df.shape)

print("\nColumn Names:")
print(df.columns.tolist())

print("\nOPE ID Duplicate Check")
print("-" * 40)

duplicate_ope_count = df["ope_id"].duplicated().sum()
print("Duplicate OPE ID count:", duplicate_ope_count)

duplicate_ope_rows = df[df["ope_id"].duplicated(keep=False)]

print("\nDuplicate OPE ID Rows:")
<<<<<<< HEAD
print(duplicate_ope_rows[["ope_id", "school", "state", "school_type"]])

print("test")
=======
print(duplicate_ope_rows[["ope_id", "school", "state", "school_type"]])
>>>>>>> b816be63cf4526c1ae2e270e1859b9a9577762ca
