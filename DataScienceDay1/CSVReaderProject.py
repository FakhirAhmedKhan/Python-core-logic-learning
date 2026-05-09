import csv
import time

# --- CSV Reader Project ---
# This program reads a CSV file and calculates statistics for student marks.

def read_and_analyze_csv(filename):
    """
    Reads the CSV file, calculates stats, and measures the time taken.
    """
    # 1. Start the timer to measure loading time
    start_time = time.time()
    
    marks_list = []
    student_count = 0

    try:
        # 2. File handling: Open the CSV file
        with open(filename, mode='r', newline='') as file:
            # Use csv.DictReader to read rows as dictionaries
            reader = csv.DictReader(file)
            
            # 3. Loop through each row in the CSV
            for row in reader:
                name = row['name']
                mark = float(row['marks']) # Convert string to number
                
                marks_list.append(mark)
                student_count += 1
        
        # 4. Measure end time
        end_time = time.time()
        loading_time = end_time - start_time

        # 5. Calculate statistics using functions
        if student_count > 0:
            total_marks = sum(marks_list)
            average_marks = total_marks / student_count
            highest_mark = max(marks_list)
            lowest_mark = min(marks_list)

            # 6. Display results in a clean format
            print("\n" + "="*40)
            print("       CSV DATA ANALYSIS REPORT       ")
            print("="*40)
            print(f"File Processed    : {filename}")
            print(f"Total Students    : {student_count}")
            print(f"Average Marks     : {average_marks:.2f}")
            print(f"Highest Mark      : {highest_mark}")
            print(f"Lowest Mark       : {lowest_mark}")
            print(f"Loading Time      : {loading_time:.6f} seconds")
            print("="*40)
        else:
            print("The CSV file is empty.")

    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    # Define the filename
    csv_file = "students.csv"
    
    print("Initializing CSV Reader Project...")
    # Call the function to process the file
    read_and_analyze_csv(csv_file)

# Run the program
if __name__ == "__main__":
    main()
