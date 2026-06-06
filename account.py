import random
class Account:
    def __init__(self, owner, balance = 0):
        self.owner = owner
        self.balance = balance
        self.transactions =[]
        self.account_number = random.randint(10000000, 99999999)

    def deposit( self, amount):
        if amount <= 0:
            print("Deposit amount must be positive. ")
            return
        self.balance += amount
        self.transactions.append(f"Deposited ${amount:.2f}")
        print(f"Deposited ${amount:.2f}. New balance: ${self.balance:.2f}")

    def withdraw(self, amount):
        if amount <=0:
            print("Amount must be positive.")
            return
        if amount > self.balance:
            print("Insufficinet funds.")
            return
        self.balance -= amount
        self.transactions.append(f"Withdrew ${amount:.2f}")
        print(f"Withdrew ${amount:.2f}. New Balance: ${self.balance:>2f}")

    def get_balance(self):
        print(f"{self.owner} 's balance: ${self.balance:.2f}")

    def get_history(self):
        if not self.transactions:
            print("No transactions yet.")
            return
        print(f"\n--- Transaction History for {self.owner} ---")
        for i, t in enumerate(self.transactions, 1):
            print(f"{i}. {t}")

    def __str__(self):
        def __str__(self):
            return f"Account[{self.owner}] — Acc#: {self.account_number} — Balance: ${self.balance:.2f}"


class SavingsAccount(Account):
    def __init__(self, owner, balance=0, interest_rate=0.05):
        super().__init__(owner, balance)
        self.interest_rate = interest_rate

    def apply_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        print(f"Interest applied: ${interest:.2f}. New balance: ${self.balance:.2f}")

    def __str__(self):
        return f"SavingsAccount[{self.owner}] — Balance: ${self.balance:.2f} | Rate: {self.interest_rate*100}%"


class CheckingAccount(Account):
    def __init__(self, owner, balance=0, overdraft_limit=100):
        super().__init__(owner, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if amount > self.balance + self.overdraft_limit:
            print(f"Exceeds overdraft limit of ${self.overdraft_limit:.2f}.")
            return
        self.transactions.append(f"Withdrew ${amount:.2f}")
        self.balance -= amount
        print(f"Withdrew ${amount:.2f}. New balance: ${self.balance:.2f}")

    def __str__(self):
        return f"CheckingAccount[{self.owner}] — Balance: ${self.balance:.2f} | Overdraft: ${self.overdraft_limit:.2f}"










        