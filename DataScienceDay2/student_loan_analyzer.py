import pandas as pd

# Load dataset
df = pd.read_csv("student_loan_data.xls")

# -----------------------------
# CLEAN COLUMN NAMES
# -----------------------------
df.columns = (
    df.columns
    .str.strip()
    .str.lower()
    .str.replace(" ", "_")
    .str.replace("#", "num")
    .str.replace("$", "amount")
)

# Example:
# "# of Loans Originated" -> "num_of_loans_originated"

# -----------------------------
# REMOVE EMPTY ROWS/COLUMNS
# -----------------------------
df.dropna(how="all", inplace=True)
df.dropna(axis=1, how="all", inplace=True)

# -----------------------------
# REMOVE DUPLICATES
# -----------------------------
df.drop_duplicates(inplace=True)

# -----------------------------
# CLEAN TEXT COLUMNS
# -----------------------------
text_cols = ["school", "state", "school_type"]

for col in text_cols:
    if col in df.columns:
        df[col] = df[col].str.strip()

# -----------------------------
# CONVERT NUMERIC COLUMNS
# -----------------------------
numeric_cols = [
    "recipients",
    "num_of_loans_originated",
    "amount_of_loans_originated",
    "num_of_loans_disbursed",
    "amount_of_loans_disbursed"
]

for col in numeric_cols:
    if col in df.columns:
        df[col] = (
            df[col]
            .astype(str)
            .str.replace(",", "")
            .str.replace("$", "")
        )

        df[col] = pd.to_numeric(df[col], errors="coerce")

# -----------------------------
# REMOVE CANCELLED LOANS
# -----------------------------
if "loan_status" in df.columns:
    df = df[df["loan_status"] != "Cancelled"]

# -----------------------------
# REMOVE ZERO DISBURSEMENTS
# -----------------------------
if "amount_of_loans_disbursed" in df.columns:
    df = df[df["amount_of_loans_disbursed"] > 0]

# -----------------------------
# SIMPLE ANALYSIS
# -----------------------------

# Total loan amount
print("Total Loan Amount:")
print(df["amount_of_loans_originated"].sum())

# Average loan amount
print("\nAverage Loan Amount:")
print(df["amount_of_loans_originated"].mean())

# Loans by state
print("\nLoans by State:")
print(
    df.groupby("state")["amount_of_loans_originated"]
    .sum()
    .sort_values(ascending=False)
)

# Top 5 schools
print("\nTop 5 Schools:")
print(
    df.groupby("school")["amount_of_loans_originated"]
    .sum()
    .sort_values(ascending=False)
    .head(5)
)

# -----------------------------
# SAVE CLEAN DATA
# -----------------------------
df.to_csv("cleaned_loan_data.csv", index=False)

print("\nCleaning Complete")