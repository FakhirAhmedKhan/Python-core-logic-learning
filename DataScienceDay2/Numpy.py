# # 1. NumPy arrays
# import numpy as np

# # # Create a NumPy array of student marks
# # marks = np.array([70, 80, 90, 60])
# # # Create a regular Python list of student marks
# # SimplePython = ([70, 80, 90, 60])

# # print(marks) # Output: [70 80 90 60]
# # print(np.mean(marks)) # Output: 75.0
# # print(np.max(marks)) # Output: 90
# # print(np.min(marks)) # Output: 60
# # print(np.argmax(marks)) # Output: 2 (index of the highest mark)
# # print(np.argmin(marks)) # Output: 3 (index of the lowest mark)
# # print(marks[0]) # Output: 70
# # print(marks[1:3]) # Output: [80 90]
# # print(SimplePython) # Output: [70, 80, 90, 60]


# # ## 2. Array indexing

# # marks = np.array([70, 80, 90, 60])
# # SimplePython = [70, 80, 90, 60]

# # print(np.add(marks[1], marks[0]))  # 80 + 70 = 150
# # print(marks[1])  # second value
# # print(marks[2])  # third value

# # print(SimplePython[1] + SimplePython[0])  # 80 + 70 = 150
# # print(SimplePython[1])  # second value
# # print(SimplePython[2])  # third value



# ## 3. Array slicing

# # marks = np.array([70, 80, 90, 60, 50])
# # SimplePython = [70, 80, 90, 60, 50]

# # print(marks[1:4]) # Output: [80 90 60]
# # print(SimplePython[1:4]) # Output: [80, 90, 60]
# # print("[" + " ".join(map(str, SimplePython[1:4])) + "]") # Output: [80 90 60]

# # loan_amounts = np.array([5000, 7000, 3000, 9000])
# # SimplePythonLoans = [5000, 7000, 3000, 9000]

# # print(np.sum(loan_amounts)) # Output: 24000
# # print(np.mean(loan_amounts))# Output: 6000.0
# # print(np.max(loan_amounts))# Output: 9000
# # print(np.min(loan_amounts))# Output: 3000

# # print(sum(SimplePythonLoans)) # Output: 24000
# # print(sum(SimplePythonLoans) / len(SimplePythonLoans)) # Output: 6000.0
# # print(max(SimplePythonLoans))# Output: 9000
# # print(min(SimplePythonLoans))# Output: 3000

# # ## 5. argmax()

# # loan_amounts = np.array([5000, 7000, 3000, 9000])
# # simple_loan_amounts = [5000, 7000, 3000, 9000]


# # highest_index = np.argmax(loan_amounts)
# # highest_index_simple = simple_loan_amounts.index(max(simple_loan_amounts))

# # print(highest_index) # Output: 3
# # print(loan_amounts[highest_index]) # Output: 9000

# # print(highest_index_simple) # Output: 3
# # print(simple_loan_amounts[highest_index_simple]) # Output: 9000


# # ## 6. axis=0 and axis=1

# # data = np.array([[5000, 5, 12],[7000, 6, 24],[3000, 4, 10]])

# # simple_data = [[5000, 5, 12],[7000, 6, 24],[3000, 4, 10]]

# # # column-wise sum axis=0 = columns
# # print(np.sum(data, axis=0)) # output: [15000    15    46]

# # # row-wise sum axis=1 = rows
# # print(np.sum(data, axis=1)) # output: [5017 7030 3014] 

# # # Column-wise sum formula without using NumPy
# # column_sum = [sum(col) for col in zip(*data)]

# # # Row-wise sum formula without using NumPy
# # row_sum = [sum(row) for row in data]

# # print("Column-wise sum:", column_sum) # Output: Column-wise sum: [np.int64(15000), np.int64(15), np.int64(46)]

# # print("Row-wise sum:", row_sum) # Output: Row-wise sum: [np.int64(5017), np.int64(7030), np.int64(3014)]

# ## 7. Rows and columns

# # data = np.array([
# #     [5000, 5, 12],
# #     [7000, 6, 24],
# #     [3000, 4, 10]
# #     ])

# # # first row
# # print(data[0])    # Output: [5000    5   12]  
# # # first column
# # print(data[:, 0])   # Output: [5000 7000 3000]


# # # 8. Basic data simplification

# # loan_amounts = np.array([5000, 7000, 3000, 9000])

# # simple_amounts = loan_amounts / 1000

# # print(simple_amounts) # output: [5. 7. 3. 9.] is the simplified version of the loan amounts in thousands


# ## 9. Moving cleaned data into a new file
# data = [
#     ["Student", "Loan Amount"],
#     ["Ali", 5000],
#     ["Ahmed", 7000],
#     ["Sara", 3000]
# ]

# with open("student_loan_cleaned.csv", "w") as file:
#     for row in data:
#         file.write(f"{row[0]},{row[1]}\n")

# print("File created successfully")

# ## 10. Real dataset handling

# loan_amounts = np.array([5000, 7000, 3000, 9000, 6000])

# total_loan = np.sum(loan_amounts)
# average_loan = np.mean(loan_amounts)
# highest_loan = np.max(loan_amounts)
# lowest_loan = np.min(loan_amounts)

# print("Total Loan:", total_loan) # Output: Total Loan: 30000
# print("Average Loan:", average_loan) # Output: Average Loan: 6000.0
# print("Highest Loan:", highest_loan) # Output: Highest Loan: 9000
# print("Lowest Loan:", lowest_loan) # Output: Lowest Loan: 3000

# ## Simple combined example

# # Student loan data
# # Columns: loan_amount, interest_rate, loan_term_months
# student_loans = np.array([
#     [5000, 5, 12],
#     [7000, 6, 24],
#     [3000, 4, 10],
#     [9000, 7, 36]
# ])

# loan_amounts = student_loans[:, 0]

# print("Loan Amounts:", loan_amounts)
# print("Total Loan:", np.sum(loan_amounts))
# print("Average Loan:", np.mean(loan_amounts))
# print("Highest Loan:", np.max(loan_amounts))
# print("Lowest Loan:", np.min(loan_amounts))
# print("Highest Loan Index:", np.argmax(loan_amounts))