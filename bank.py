from account import (
    Account, SavingsAccount, CheckingAccount,
    InsufficientFundsError, InvalidAmountError, OverdraftLimitExceededError
)

def show_menu():
    print("\n--- Chase Bank Menu ---")
    print("1. Check balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Apply interest (Savings only)")
    print("5. Transaction history")
    print("6. Undo last transaction")
    print("7. Exit")
    

def main():
    print("Welcome to Chase Bank!")
    name = input("Enter your name: ")
    acc_type = input("Account type (checking/savings): ").lower()

    if acc_type == "savings":
        account = SavingsAccount(name, 0, 0.05)
    elif acc_type == "checking":
        account = CheckingAccount(name, 0, 100)
    else:
        account = Account(name, 0)

    print(f"\nAccount created!")
    print(f"Account Number: {account.account_number}")
    print(f"Account Type: {account}")

    while True:
        show_menu()
        choice = input("Choose: ")

        if choice == "1":
            account.get_balance()
        elif choice == "2":
            amount = float(input("Deposit amount: $"))
            try:
                account.deposit(amount)
            except InvalidAmountError as e:
                print(f"Deposit failed: {e}")
        elif choice == "3":
            amount = float(input("Withdraw amount: $"))
            try:
                account.withdraw(amount)
            except OverdraftLimitExceededError as e:
                print(f"Withdrawal failed (overdraft): {e}")
            except InsufficientFundsError as e:
                print(f"Withdrawal failed: {e}")
            except InvalidAmountError as e:
                print(f"Withdrawal failed: {e}")
        elif choice == "4":
            if isinstance(account, SavingsAccount):
                account.apply_interest()
            else:
                print("Only savings accounts earn interest.")
        elif choice == "5":
            account.get_history()
        elif choice == "6":
             account.undo()
        elif choice == "7":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")

main()