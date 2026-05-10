import pandas as pd
import numpy as np

# Input file
input_file = "student_loan_data.csv"

# Output file
output_file = "student_loan_data.xls"

# Read CSV data
df = pd.read_csv(input_file)

# Clean column names
df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

# Remove duplicate rows
df = df.drop_duplicates()

# Fill missing numeric values with 0
numeric_cols = df.select_dtypes(include=[np.number]).columns
df[numeric_cols] = df[numeric_cols].fillna(0)

# Fill missing text values with "Unknown"
text_cols = df.select_dtypes(include=["object"]).columns
df[text_cols] = df[text_cols].fillna("Unknown")

# Example simplification
# Keep only important columns if they exist
important_columns = [
    "student_id",
    "student_name",
    "loan_amount",
    "interest_rate",
    "loan_term",
    "monthly_payment"
]

available_columns = [col for col in important_columns if col in df.columns]
df_simple = df[available_columns]

# If monthly_payment does not exist, calculate simple monthly payment
if "monthly_payment" not in df_simple.columns:
    if "loan_amount" in df_simple.columns and "loan_term" in df_simple.columns:
        df_simple["monthly_payment"] = np.where(
            df_simple["loan_term"] > 0,
            df_simple["loan_amount"] / df_simple["loan_term"],
            0
        )

# Save to XLS file
df_simple.to_excel(output_file, index=False, engine="xlwt")

print("✅ Simplified XLS file created:", output_file)