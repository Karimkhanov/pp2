class BankAccount:
    def __init__(self, owner, balance=0.0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"{amount} has been deposited to your account. Your current balance is {self.balance}.")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Withdrawal amount exceeds available balance.")
        else:
            self.balance -= amount
            print(f"{amount} has been withdrawn from your account. Your current balance is {self.balance}.")
    def owner_name(self, name):
        self.name = name
# Create a new BankAccount object
account = BankAccount("John Doe")

# Make some deposits
account.deposit(int(input()))
account.deposit(int(input()))

# Make some withdrawals
account.withdraw(int(input()))
account.withdraw(int(input()))
account.owner_name(print(input("Owners name:")))
