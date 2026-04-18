# Python Expense Tracker (CLI + CSV) 
# expense_tracker.py 
# CLI Command Line Interface 
# CSV Comma Seprated Values File 

import csv 
import os 

FILENAME = "expenses.csv" 

# Create the file with headers if it doesn't exist 
if not os.path.exists(FILENAME): 
    with open(FILENAME, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Amount", "Category", "Description"]) 

def add_expenses(): 
    amount = float(input("Enter amount: ₹")) 
    category = input("Enter category (Food/Travel/Bills/Other): ")
    desc = input("Enter description: ") 

    with open(FILENAME, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([amount, category, desc]) 

    print("Expenses added successfully!\n") 

def view_expenses():
    with open(FILENAME, "r") as f:
        reader = csv.reader(f)
        next(reader) # skip header
        print("\n--- Expenses List ---") 
        for row in reader:
            print(f"{row[0]} | {row[1]} | {row[2]}") 
        print() 

def total_expenses():
    total = 0
    with open(FILENAME, "r") as f:
        reader = csv.reader(f)
        next(reader)
        for row in reader:
            total += float(row[0]) 
        print(f"\nTotal Spending: ₹{total}\n") 

def filter_by_category():
    cat = input("Enter category to filter: ") 
    print(f"\n--- Expenses in {cat} ---")
    found = False

    with open(FILENAME, "r") as f:
        reader = csv.reader(f)
        next(reader)
        for row in reader:
            if row[1].lower() == cat.lower():
                print(f"₹{row[0]} | {row[2]}")
                found = True 

    if not found:
        print("No expenses found in this category.")
    print() 

def menu():
    while True:
        print("======= Expense Tracker =======")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. Total Spending")
        print("4. Filter by Category")
        print("5. Exit") 

        choice = input("Enter choice: ") 

        if choice == "1":
            add_expenses() 
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            total_expenses() 
        elif choice == "4":
            filter_by_category()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice! Try again.\n") 

menu() 


