import csv

# --- Expense Tracker Project ---
# This program allows users to manage their expenses and save them to a file.

# Global list to store expense dictionaries
expenses = []

def add_expense():
    """Asks user for expense details and adds to the list."""
    print("\n--- Add New Expense ---")
    title = input("Enter expense title (e.g., Lunch): ")
    try:
        amount = float(input("Enter amount: "))
        category = input("Enter category (e.g., Food, Travel, Bills): ")
        
        # Store as a dictionary
        expense = {
            "title": title,
            "amount": amount,
            "category": category
        }
        expenses.append(expense)
        print("Expense added successfully!")
    except ValueError:
        print("Invalid amount! Please enter a number.")

def view_expenses():
    """Displays all expenses currently in the list."""
    if not expenses:
        print("\nNo expenses found.")
        return

    print("\n--- All Expenses ---")
    print(f"{'Title':<15} | {'Amount':<10} | {'Category':<15}")
    print("-" * 45)
    for exp in expenses:
        print(f"{exp['title']:<15} | ${exp['amount']:<9.2f} | {exp['category']:<15}")

def show_total():
    """Calculates and shows the sum of all expenses."""
    total = sum(exp['amount'] for exp in expenses)
    print(f"\nTotal Spending: ${total:.2f}")

def show_category_summary():
    """Groups expenses by category and shows totals for each."""
    if not expenses:
        print("\nNo expenses to categorize.")
        return

    summary = {}
    for exp in expenses:
        cat = exp['category']
        summary[cat] = summary.get(cat, 0) + exp['amount']

    print("\n--- Category-wise Spending ---")
    for cat, total in summary.items():
        print(f"{cat}: ${total:.2f}")

def save_to_csv():
    """Saves the list of dictionaries into expenses.csv."""
    if not expenses:
        print("\nNothing to save.")
        return

    filename = "expenses.csv"
    try:
        with open(filename, mode='w', newline='') as file:
            fieldnames = ["title", "amount", "category"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            
            writer.writeheader()
            writer.writerows(expenses)
        print(f"Data saved successfully to {filename}!")
    except Exception as e:
        print(f"Error saving file: {e}")

def main():
    while True:
        print("\n" + "="*30)
        print("      EXPENSE TRACKER")
        print("="*30)
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. Show Total Expense")
        print("4. Show Category Summary")
        print("5. Save to CSV")
        print("6. Exit")
        
        choice = input("\nChoose an option (1-6): ")

        if choice == '1':
            add_expense()
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            show_total()
        elif choice == '4':
            show_category_summary()
        elif choice == '5':
            save_to_csv()
        elif choice == '6':
            print("Exiting Expense Tracker. Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
