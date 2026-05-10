

## 1. NumPy arrays

import numpy as np

marks = np.array([70, 80, 90, 60])

print(marks)

# Output:[70 80 90 60]

## 2. Array indexing


marks = np.array([70, 80, 90, 60])

print(marks[0])  # first value
print(marks[2])  # third value

# Output:

# ```text
# 70
# 90
# ```

## 3. Array slicing


marks = np.array([70, 80, 90, 60, 50])

print(marks[1:4])
# ```

# Output:

# ```text
# [80 90 60]
# ```

## 4. sum(), mean(), max(), min()


loan_amounts = np.array([5000, 7000, 3000, 9000])

print(np.sum(loan_amounts))
print(np.mean(loan_amounts))
print(np.max(loan_amounts))
print(np.min(loan_amounts))
# ```

# Output:

# ```text
# 24000
# 6000.0
# 9000
# 3000
# ```

## 5. argmax()

loan_amounts = np.array([5000, 7000, 3000, 9000])

highest_index = np.argmax(loan_amounts)

print(highest_index)
print(loan_amounts[highest_index])
# ```

# Output:

# ```text
# 3
# 9000
# ```

## 6. axis=0 and axis=1

data = np.array([
    [5000, 5, 12],
    [7000, 6, 24],
    [3000, 4, 10]
])

print(np.sum(data, axis=0))  # column-wise sum
print(np.sum(data, axis=1))  # row-wise sum

# Output:

# ```text
# [15000    15    46]
# [5017 7030 3014]

# Meaning:

# ```text
# axis=0 = columns
# axis=1 = rows
# ```

## 7. Rows and columns

data = np.array([
    [5000, 5, 12],
    [7000, 6, 24],
    [3000, 4, 10]
])

print(data[0])      # first row
print(data[:, 0])   # first column
# ```

# Output:

# ```text
# [5000    5   12]
# [5000 7000 3000]
# ```

## 8. Basic data simplification

loan_amounts = np.array([5000, 7000, 3000, 9000])

simple_amounts = loan_amounts / 1000

print(simple_amounts)
# ```

# Output:

# ```text
# [5. 7. 3. 9.]
# ```

# Meaning:

# ```text
# 5000 becomes 5k
# 7000 becomes 7k
# ```

## 9. Moving cleaned data into a new file
data = [
    ["Student", "Loan Amount"],
    ["Ali", 5000],
    ["Ahmed", 7000],
    ["Sara", 3000]
]

with open("student_loan_cleaned.csv", "w") as file:
    for row in data:
        file.write(f"{row[0]},{row[1]}\n")

print("File created successfully")

## 10. Real dataset handling

loan_amounts = np.array([5000, 7000, 3000, 9000, 6000])

total_loan = np.sum(loan_amounts)
average_loan = np.mean(loan_amounts)
highest_loan = np.max(loan_amounts)
lowest_loan = np.min(loan_amounts)

print("Total Loan:", total_loan)
print("Average Loan:", average_loan)
print("Highest Loan:", highest_loan)
print("Lowest Loan:", lowest_loan)
# ```

# Output:

# ```text
# Total Loan: 30000
# Average Loan: 6000.0
# Highest Loan: 9000
# Lowest Loan: 3000
# ```

## Simple combined example

# Student loan data
# Columns: loan_amount, interest_rate, loan_term_months
student_loans = np.array([
    [5000, 5, 12],
    [7000, 6, 24],
    [3000, 4, 10],
    [9000, 7, 36]
])

loan_amounts = student_loans[:, 0]

print("Loan Amounts:", loan_amounts)
print("Total Loan:", np.sum(loan_amounts))
print("Average Loan:", np.mean(loan_amounts))
print("Highest Loan:", np.max(loan_amounts))
print("Lowest Loan:", np.min(loan_amounts))
print("Highest Loan Index:", np.argmax(loan_amounts))