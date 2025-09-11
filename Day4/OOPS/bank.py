class BankAccount:
    def __init__(slef, balance=0):
        slef.__balance = balance # private variable
    
    def deposit(slef, amount):
        if amount>0:
            slef.__balance+= amount
        else:
            print("Deposit amount must be positive")
    
    def withdraw(slef, amount):
        if amount > 0:
            if amount <= slef.__balance:
                slef.__balance -= amount
            else:
                print("Insufficient balance")
        else:
            print("Withdraw amount must be positive")
    
    def get_balance(slef):
        return slef.__balance


# creating an object of Bank Account
account = BankAccount(1000)
print("Initial balance:", account.get_balance())

account.deposit(10000)
print("Balance after deposit:", account.get_balance())

account.withdraw(5000)
print("Balance after withdrawal:", account.get_balance())

# creating another object of Bank Account
account2 = BankAccount()
# trying to access the private variable directly
#print(account2.__balance)  # AttributeError: 'BankAccount' object has no attribute '__balance'
# correct way to access the balance
print("Initial balance of account2:", account2.get_balance())
account2.deposit(2000)
print("Balance of account2 after deposit:", account2.get_balance())
account2.withdraw(1000)
print("Balance of account2 after withdrawal:", account2.get_balance())
account2.withdraw(5000)  # Insufficient balance
print("Final balance of account2:", account2.get_balance())