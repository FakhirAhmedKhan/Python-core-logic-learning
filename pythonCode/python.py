## Day 1 Study Plan

# name = "Ansari"
# age = 25
# salary = 5000.50
# is_learning = True

# print(name)
# print(age)
# print(salary)
# print(is_learning)

# text = "Python"
# number = 10
# decimal = 10.5
# status = True

# print(type(text))
# print(type(number))
# print(type(decimal))
# print(type(status))

# marks = [80, 75, 90, 65, 88]

# print(marks)
# print(marks[0])
# print(marks[-1])
# print(len(marks))
# print(sum(marks))

# average = sum(marks) / len(marks)

# print("Average:", average)

# student = {
#     "name": "Ali",
#     "age": 22,
#     "course": "Data Science",
#     "marks": 85
# }

# print(student["name"])
# print(student["course"])

# marks = 72

# if marks >= 80:
#     print("Grade A")
# elif marks >= 60:
#     print("Grade B")
# else:
#     print("Grade C")

# marks = [80, 75, 90, 65, 88]

# for mark in marks:
#     print(mark)

# total = 0

# for mark in marks:
#     total = total + mark

# average = total / len(marks)
# print("Average:", average)


# def calculate_average(marks):
#     return sum(marks) / len(marks)

# student_marks = [80, 75, 90, 65, 88]

# average = calculate_average(student_marks)
# print("Average:", average)

# students = [
#     {"name": "Ali", "marks": [80, 75, 90]},
#     {"name": "Sara", "marks": [60, 70, 65]},
#     {"name": "Ahmed", "marks": [90, 95, 88]},
# ]

# def calculate_average(marks):
#     return sum(marks) / len(marks)

# def get_grade(average):
#     if average >= 80:
#         return "A"
#     elif average >= 60:
#         return "B"
#     else:
#         return "C"

# for student in students:
#     average = calculate_average(student["marks"])
#     grade = get_grade(average)

#     print("Name:", student["name"])
#     print("Average:", average)
#     print("Grade:", grade)
#     print("-" * 20)
    
    
    
# read file by python code basic
# import csv

# with open("data.csv", "r") as file:
#  reader = csv.reader(file)
#  for row in reader: print(row)
 
 
import csv
import time

start_time = time.time()

with open("data.csv", "r") as file:
    reader = csv.reader(file)
    rows = list(reader)

end_time = time.time()

total_time = end_time - start_time

print(f"Total rows read: {len(rows)}")
print(f"CSV read time: {total_time:.4f} seconds")