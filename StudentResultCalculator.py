# --- Student Result Calculator ---
# This program calculates the total, average, and grade for a student.

def calculate_grade(average):
    """
    Function to determine the grade based on the average marks.
    Uses if-elif-else conditions.
    """
    if average >= 90:
        return "A+"
    elif average >= 80:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 50:
        return "D"
    else:
        return "Fail"

def main():
    # 1. Ask for the student's name
    print("Welcome to the Student Result Calculator!")
    student_name = input("Enter student name: ")

    # 2. Initialize an empty list to store marks
    marks = []

    # 3. Ask for marks in 5 subjects using a loop
    print("\nPlease enter marks for 5 subjects (out of 100):")
    for i in range(1, 6):
        while True:
            try:
                # Get input and convert to a number (float)
                mark = float(input(f"Enter marks for Subject {i}: "))
                
                # Simple validation to ensure marks are between 0 and 100
                if 0 <= mark <= 100:
                    marks.append(mark)
                    break
                else:
                    print("Please enter a valid mark between 0 and 100.")
            except ValueError:
                print("Invalid input! Please enter a number.")

    # 4. Calculate total marks using the built-in sum() function
    total_marks = sum(marks)

    # 5. Calculate average marks
    average_marks = total_marks / 5

    # 6. Get the grade by calling our function
    grade = calculate_grade(average_marks)

    # 7. Show the final result clearly
    print("\n" + "="*30)
    print("       FINAL RESULT       ")
    print("="*30)
    print(f"Student Name  : {student_name}")
    print(f"Marks obtained: {marks}")
    print(f"Total Marks   : {total_marks} / 500")
    print(f"Average Marks : {average_marks:.2f}") # .2f formats to 2 decimal places
    print(f"Grade         : {grade}")
    print("="*30)

# This ensures the main function runs when the script is executed
if __name__ == "__main__":
    main()
