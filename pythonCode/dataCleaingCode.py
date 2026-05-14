import pandas as pd
import os

# Define file path
file_path = r'c:\Users\Dell\OneDrive\Desktop\Programs\Python-core-logic-learning\DataScienceDay3\data.csv'

# Read the data
try:
    df = pd.read_csv(file_path)
except Exception as e:
    print(f"Error reading file: {e}")
    exit(1)

# 1. How many schools are in the dataset?
school_count = df['school'].nunique()

# 2. How many states are included?
state_count = df['state'].nunique()

# 3. Which state has the most schools?
state_most_schools = df['state'].value_counts().idxmax()
state_most_schools_count = df['state'].value_counts().max()

# 4. Which school type is most common?
most_common_type = df['school_type'].value_counts().idxmax()
most_common_type_count = df['school_type'].value_counts().max()

# 5. Which schools have the highest loan amount?
# Calculating total loan amount by summing relevant columns
loan_columns = [
    'subsidized_loans_originated_amount',
    'unsubsidized_loans_originated_amount',
    'parent_plus_loans_originated_amount',
    'grad_plus_loans_originated_amount'
]
df['total_loan_amount'] = df[loan_columns].sum(axis=1)
highest_loan_schools = df.nlargest(5, 'total_loan_amount')[['school', 'total_loan_amount']]

# 6. Are there missing values?
missing_values = df.isnull().sum()
any_missing = missing_values.any()

# 7. Are there duplicate OPE IDs?
duplicate_ope_ids = df['ope_id'].duplicated().any()

# 8. What are the top 10 states by school count?
top_10_states = df['state'].value_counts().head(10)

# Output results
print(f"--- Analysis Results ---")
print(f"1. Total schools (unique): {school_count}")
print(f"2. Total states: {state_count}")
print(f"3. State with most schools: {state_most_schools} ({state_most_schools_count} schools)")
print(f"4. Most common school type: {most_common_type} ({most_common_type_count} schools)")
print(f"\n5. Schools with highest total loan amount:")
print(highest_loan_schools.to_string(index=False))
print(f"\n6. Are there missing values? {'Yes' if any_missing else 'No'}")
if any_missing:
    print(missing_values[missing_values > 0])
print(f"7. Are there duplicate OPE IDs? {'Yes' if duplicate_ope_ids else 'No'}")
print(f"\n8. Top 10 states by school count:")
print(top_10_states)

