class Account:
    def __init__(self, owner):
        self.owner = owner
        self.balance = 0
        self.closed = False

    def deposit(self, amount):
        if self.closed:
            raise RuntimeError("Account is closed")
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if self.closed:
            raise RuntimeError("Account is closed")
        if amount <= 0:
            raise ValueError("Withdraw amount must be positive")
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        self.balance -= amount
        return self.balance

    def close(self):
        self.closed = True
