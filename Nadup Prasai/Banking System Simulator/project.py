def Create_Account():
    """Create a new account."""
    print("\n--- Create Account ---")
    name = input("Enter your name: ")
    while True:
        try:
            starting_balance = float(input("Enter starting balance: "))
            if starting_balance < 0:
                print("Starting balance cannot be negative. Try again.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    account = {"name": name, "balance": starting_balance}
    print(f"Account created successfully for {name} with balance {starting_balance:.2f}!\n")
    return account
    
def Deposit(account):
    
    """Deposit money into the account."""
    print("\n--- Deposit Money ---")
    while True:
        try:
            amount = float(input("Enter the amount to deposit: "))
            if amount <= 0:
                print("Deposit amount must be greater than 0. Try again.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    account["balance"] += amount
    print(f"{amount:.2f} deposited successfully! New balance: {account['balance']:.2f}\n")


def Withdraw(account):
    """Withdraw money from the account."""
    print("\n--- Withdraw Money ---")
    while True:
        try:
            amount = float(input("Enter the amount to withdraw: "))
            if amount <= 0:
                print("Withdrawal amount must be greater than 0. Try again.")
            elif amount > account["balance"]:
                print(f"Insufficient balance! Current balance: {account['balance']:.2f}")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    account["balance"] -= amount
    print(f"{amount:.2f} withdrawn successfully! New balance: {account['balance']:.2f}\n")


def Check_Balance(account):
    """Display the current balance."""
    print("\n--- Check Balance ---")
    print(f"Account holder: {account['name']}")
    print(f"Current balance: {account['balance']:.2f}\n")



def main():
    #This is where our program starts ad we provide Main menu for our Banking System.
    print("Welcome to our Banking System")

    account = Create_Account()

    while True:
        print("---Our Services---")
        print("1 : Deposit Amount")
        print("2 : Withdraw Amount")
        print("3 : Check Balance")
        print("4 : System Exit")

        choice = input("Enter any service you want by Choosing any number from (1-4)")
        if choice == "1":
            Deposit(account)
        elif choice == "2":
            Withdraw(account)
        elif choice == "3":
            Check_Balance(account)
        elif choice == "4":
            print("\nThank you for using the Simple Banking System. Goodbye!")
            break    
        else:
            print(" INVALID CHOICE. Please Choose the valid option.")

if __name__ == "__main__":
    main()