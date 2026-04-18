# Mini Banking System with Multiple Users + PIN Login + Transaction History

# Dictionary to store accounts {account_number: {"pin": pin, "balance": balance, "history": []}} 
accounts = {
    "101": {"pin": "1234", "balance": 1000.0, "history": []},
    "102": {"pin": "2222", "balance": 500.0, "history": []},
    "103": {"pin": "3333", "balance": 2000.0, "history": []},  

} 

def create_account(account_number, pin):
    if account_number in accounts:
        return "Account already exists!" 
    else:
        accounts[account_number] = {"pin": pin, "balance": 0.0, "history": []}
        return f"Account {account_number} created successfully with balance ₹0.0"

def login(account_number, pin):
    if account_number in accounts and accounts[account_number]["pin"] == pin:
        return True 
    else:
        return False 

def deposit(account_number, amount):
    accounts[account_number]["balance"] += amount 
    accounts[account_number]["history"].append(f"Deposited  ₹{amount}") 
    return f"₹{amount} deposited successfully! Current balance: ₹{accounts[account_number]["balance"]}" 

def withdraw(account_number, amount):
    if amount > accounts[account_number]["balance"]:
        return "Insufficient balance!"  
    else:
        accounts[account_number]["balance"] -= amount 
        accounts[account_number]["history"].append(f"Withdraw ₹{amount}") 
        return f"₹{amount} withdrawn successfully! Current balance: ₹{accounts[account_number]["balance"]}"

def check_balance(account_number):
    return f"Your current balance is: ₹{accounts[account_number]["balance"]}"

def show_history(account_number): 
    history = accounts[account_number]["history"] 
    if not history:
        return "No transaction yet."
    else:
        return "\n".join(history)


# Main Program
print("----- Welcome to Mini Banking System -----")

while True:
    print("\nChoose an option: ") 
    print("1. Create Account") 
    print("2. Login")
    print("3. Exit") 

    choice = input("Enter your choice (1/2/3): ")

    if choice == "1":
        acc = input("Enter new account number: ")
        pin = input("Set a 4-digit PIN: ")
        print(create_account(acc, pin)) 
    
    elif choice == "2":
        acc = input("Enter account number: ")
        pin = input("Enter PIN: ") 

        if login(acc, pin):
            print(f"\nLogin successful! Welcome, Account {acc} 🎉") 

            while True:
                print(f"\nBanking Menu:") 
                print("1. Deposit")
                print("2. Withdraw")
                print("3. Check Balance") 
                print("4. Transaction History")
                print("5. Logout") 
                
                option = input("Enter choice (1/2/3/4/5): ") 

                if option == "1":
                    amt = float(input("Enter amount to deposit: ")) 
                    print(deposit(acc, amt)) 
                
                elif option == "2":
                    amt = float(input("Enter amount to withdraw: "))
                    print(withdraw(acc, amt)) 

                elif option == "3":
                    print(check_balance(acc)) 

                elif option == "4":
                    print("\n--- Transaction History ---") 
                    print(show_history(acc)) 

                elif option == "5":
                    print("Logged out successfully ✅")
                    break 

                else: 
                    print("Invalid option!") 

        else: 
            print("Invalid account number or PIN ❌") 

    elif choice == "3":
        print("Thank you for using Mini Banking System 😊")
        break 

    else:
        print("Invalid choice! Please try again.") 

