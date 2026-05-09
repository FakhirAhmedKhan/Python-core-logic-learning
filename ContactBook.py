import csv
import os

# --- Contact Book Project ---
# A simple system to manage contact information.

FILENAME = "contacts.csv"
# We use a dictionary where 'name' is the key for fast searching
contacts = {}

def load_contacts():
    """Reads contacts from CSV file at startup."""
    if os.path.exists(FILENAME):
        try:
            with open(FILENAME, mode='r', newline='') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    # Store phone and email inside another dictionary
                    contacts[row['name']] = {
                        "phone": row['phone'],
                        "email": row['email']
                    }
            print("Contacts loaded successfully.")
        except Exception as e:
            print(f"Error loading contacts: {e}")

def save_contacts():
    """Writes the current dictionary to a CSV file."""
    try:
        with open(FILENAME, mode='w', newline='') as file:
            fieldnames = ["name", "phone", "email"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            
            # Prepare rows from the dictionary
            for name, info in contacts.items():
                writer.writerow({
                    "name": name,
                    "phone": info['phone'],
                    "email": info['email']
                })
        print("Contacts saved to file!")
    except Exception as e:
        print(f"Error saving contacts: {e}")

def add_contact():
    name = input("Enter name: ").strip()
    if name in contacts:
        print("Contact already exists!")
        return
    
    phone = input("Enter phone number: ")
    email = input("Enter email address: ")
    
    contacts[name] = {"phone": phone, "email": email}
    print(f"Contact '{name}' added!")

def view_all():
    if not contacts:
        print("\nNo contacts found.")
        return
    
    print("\n" + "-"*40)
    print(f"{'Name':<15} | {'Phone':<12} | {'Email'}")
    print("-"*40)
    for name, info in contacts.items():
        print(f"{name:<15} | {info['phone']:<12} | {info['email']}")

def search_contact():
    name = input("Enter name to search: ")
    if name in contacts:
        info = contacts[name]
        print(f"\nFound: {name}")
        print(f"Phone: {info['phone']}")
        print(f"Email: {info['email']}")
    else:
        print("Contact not found.")

def update_contact():
    name = input("Enter name of contact to update: ")
    if name in contacts:
        print("Enter new details (leave blank to keep current):")
        new_phone = input(f"New Phone [{contacts[name]['phone']}]: ")
        new_email = input(f"New Email [{contacts[name]['email']}]: ")
        
        if new_phone: contacts[name]['phone'] = new_phone
        if new_email: contacts[name]['email'] = new_email
        print("Contact updated!")
    else:
        print("Contact not found.")

def delete_contact():
    name = input("Enter name to delete: ")
    if name in contacts:
        del contacts[name]
        print(f"Contact '{name}' deleted.")
    else:
        print("Contact not found.")

def main():
    load_contacts()
    
    while True:
        print("\n" + "="*30)
        print("      CONTACT BOOK")
        print("="*30)
        print("1. Add Contact")
        print("2. View All Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Save Contacts")
        print("7. Exit")
        
        choice = input("\nChoose an option (1-7): ")

        if choice == '1': add_contact()
        elif choice == '2': view_all()
        elif choice == '3': search_contact()
        elif choice == '4': update_contact()
        elif choice == '5': delete_contact()
        elif choice == '6': save_contacts()
        elif choice == '7':
            save_contacts()
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
