import time
import json
import random

def login():
    username = "Fidanisma"
    password = "IloveGermany49"
    attempts = 3
    while attempts > 0:
        u = input("Username: ")
        p = input("Password: ")
        if u == username and p == password:
            print("Access granted.")
            return True
        else:
            attempts -= 1
            print(f"Incorrect credentials. Attempts left: {attempts}")
    print("Too many failed attempts. Exiting program.")
    return False
def show_motivation():
    messages = [
        "🏋️ No pain, no gain!",
        "🔥 Push harder than yesterday!",
        "💪 You are stronger than you think!",
        "🚀 Progress is progress, no matter how small.",
        "🎯 Stay focused and never give up!"
    ]
    print("\n✨ Motivation: " + random.choice(messages) + "\n")
members = []
def welcome_screen():
    CYAN = '\033[96m'
    LIGHT_CYAN = '\033[96m'
    RESET = '\033[0m'
    BOLD = '\033[1m'

    def print_welcome():
        ascii_art = r"""
     ██████╗  __     __   ██████╗ 
    ██╔════╝  \ \   / / ██╔═══  ██╗
    ██║  ███╗  \ \_/ /  ██║     ██║
    ██║   ██║   \   /   ██      ██║
    ╚██████╔╝    | |    ╚█     ██╔╝
     ╚═════╝     |_|     ╚═════╝ 
    """
        print(f"{CYAN}{BOLD}{ascii_art}{RESET}")
        print(f"{LIGHT_CYAN}Welcome to Gym Membership System!{RESET}")

    if __name__ == "__main__":
        print_welcome()
        show_motivation()
    time.sleep(1)

# Task 2: Main menu
def main_menu():
    print("\nMain Menu:")
    print("1. Add New Member")
    print("2. View All Members")
    print("3. Search Member")
    print("4. Update Member")
    print("5. Delete Member")
    print("6. Summary Statistics")
    print("7. Save to File")
    print("8. Load from File")
    print("9. Help")
    print("10. Clear All Data")
    print("0. Exit")
def add_member():
    try:
        member_id = input("Enter Member ID: ")
        name = input("Enter Name: ")
        age = int(input("Enter Age: "))
        balance = float(input("Enter Balance: "))
        members.append({'ID': member_id, 'Name': name, 'Age': age, 'Balance': balance})
        print(" Member added.")
    except ValueError:
        print(" Invalid input. Age and Balance must be numbers.")

# Task 4: Store using list of dicts (already used)

# Task 5: View all members
def view_members():
    if not members:
        print(" No records found.")
        return
    for m in members:
        try:
            balance = float(m['Balance'])  # Əmin ol ki, balance float-dır
        except (ValueError, TypeError):
            print(f"️ Warning: Invalid balance for member {m['Name']}. Skipping...")
            continue
        print(f"ID: {m['ID']} | Name: {m['Name']} | Age: {m['Age']} | Balance: ${balance:.2f}")
    original_balance = m['Balance']
    if original_balance >= 100:
        discount_rate = 0.20
    elif original_balance >= 50:
        discount_rate = 0.10
    else:
        discount_rate = 0.0

    discounted_balance = original_balance * (1 - discount_rate)

    print(f"ID: {m['ID']} | Name: {m['Name']} | Age: {m['Age']} | "
          f"Original Balance: ${original_balance:.2f} | "
          f"Discounted: ${discounted_balance:.2f} ({int(discount_rate * 100)}% off)")

def search_member():
    keyword = input("Enter ID or Name to search: ").lower()
    found = [m for m in members if keyword in m['ID'].lower() or keyword in m['Name'].lower()]
    if found:
        for m in found:
            print(f"ID: {m['ID']} | Name: {m['Name']} | Age: {m['Age']} | Balance: ${m['Balance']:.2f}")
    else:
        print(" No match found.")

# Task 7: Update member
def update_member():
    member_id = input("Enter ID to update: ")
    for m in members:
        if m['ID'] == member_id:
            m['Name'] = input("Enter new name: ")
            try:
                m['Age'] = int(input("Enter new age: "))
                m['Balance'] = float(input("Enter new balance: "))
                print(" Member updated.")
            except ValueError:
                print(" Invalid age or balance.")
            return
    print(" Member not found.")

# Task 8: Delete member
def delete_member():
    member_id = input("Enter ID to delete: ")
    global members
    members = [m for m in members if m['ID'] != member_id]
    print(" Member deleted if ID was found.")

# Task 10: Summary statistics
def summary_statistics():
    if not members:
        print(" No data for statistics.")
        return
    avg_age = sum(m['Age'] for m in members) / len(members)
    total_balance = sum(m['Balance'] for m in members)
    print(f" Average Age: {avg_age:.2f}")
    print(f" Total Balance: ${total_balance:.2f}")

# Task 11: Save to file
def save_to_file():
    with open("members.json", "w") as f:
        json.dump(members, f)
    print("Data saved to members.json.")

def load_from_file():
    global members
    try:
        with open("members.json", "r") as f:
            members = json.load(f)
            for m in members:
                m['Age'] = int(m['Age'])
                m['Balance'] = float(m['Balance'])
        print(" Data loaded from file.")
    except FileNotFoundError:
        print(" File not found.")

# Task 16: Sort by name
def sort_members():
    if not members:
        print(" No records to sort.")
        return
    sorted_list = sorted(members, key=lambda m: m['Name'])
    for m in sorted_list:
        print(f"{m['Name']} - ID: {m['ID']}, Age: {m['Age']}, Balance: ${m['Balance']:.2f}")

# Task 17: Recursive count
def count_recursive(index=0):
    if index >= len(members):
        return 0
    return 1 + count_recursive(index + 1)

# Task 18: Help menu
def help_menu():
    print("""
 Help - Menu Options:
1 - Add a new gym member
2 - View all saved members
3 - Search by ID or name
4 - Update a member's data
5 - Delete a member
6 - Show average age and total balance
7 - Save all data to file
8 - Load data from file
9 - View help
10 - Clear all records
0 - Exit
""")

# Task 19: Clear all data
def clear_all_data():
    confirm = input("Are you sure you want to delete ALL data? (yes/no): ").lower()
    if confirm == 'yes':
        members.clear()
        print(" All data cleared.")
    else:
        print(" Cancelled.")

# Main loop
def run():
    welcome_screen()
    while True:
        main_menu()
        try:
            choice = int(input("Enter your choice: "))
            if choice == 1:
                add_member()
            elif choice == 2:
                view_members()
            elif choice == 3:
                search_member()
            elif choice == 4:
                update_member()
            elif choice == 5:
                delete_member()
            elif choice == 6:
                summary_statistics()
            elif choice == 7:
                save_to_file()
            elif choice == 8:
                load_from_file()
            elif choice == 9:
                help_menu()
            elif choice == 10:
                clear_all_data()
            elif choice == 0:
                print(" Goodbye!")
                break
            else:
                print(" Invalid choice.")
        except ValueError:
            print(" Please enter a valid number.")

# Run the program
if login():
    run()