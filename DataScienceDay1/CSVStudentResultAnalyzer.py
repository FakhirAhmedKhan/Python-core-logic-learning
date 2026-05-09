import csv

# --- CSV Student Result Analyzer ---
# This project reads student data from a CSV and performs a full analysis.

def get_grade(marks):
    """Assigns a grade based on marks."""
    if marks >= 90:
        return "A+"
    elif marks >= 80:
        return "A"
    elif marks >= 70:
        return "B"
    elif marks >= 60:
        return "C"
    elif marks >= 50:
        return "D"
    else:
        return "Fail"

def analyze_results(filename):
    """Reads CSV, processes data, and displays results."""
    student_data = []
    
    try:
        # 1. Read the CSV file
        with open(filename, mode='r', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                # Convert marks to integer
                row['marks'] = int(row['marks'])
                # Assign grade
                row['grade'] = get_grade(row['marks'])
                student_data.append(row)

        # 2. Perform Calculations
        total_students = len(student_data)
        all_marks = [s['marks'] for s in student_data]
        
        if total_students > 0:
            avg_marks = sum(all_marks) / total_students
            highest = max(all_marks)
            lowest = min(all_marks)

            # 3. Show Each Student Result
            print("\n" + "="*50)
            print(f"{'NAME':<12} | {'SUBJECT':<10} | {'MARKS':<5} | {'GRADE'}")
            print("-" * 50)
            for s in student_data:
                print(f"{s['name']:<12} | {s['subject']:<10} | {s['marks']:<5} | {s['grade']}")

            # 4. Show Final Summary
            print("="*50)
            print("                RESULT SUMMARY                ")
            print("="*50)
            print(f"Total Students processed: {total_students}")
            print(f"Average Marks          : {avg_marks:.2f}")
            print(f"Highest Marks          : {highest}")
            print(f"Lowest Marks           : {lowest}")
            print("="*50)
        else:
            print("No data found in the CSV file.")

    except FileNotFoundError:
        print(f"Error: '{filename}' not found. Please create the file first.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def main():
    csv_filename = "students.csv"
    print("Initializing Student Result Analyzer...")
    analyze_results(csv_filename)

if __name__ == "__main__":
    main()