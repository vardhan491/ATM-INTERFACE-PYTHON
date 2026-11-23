class BankAccount:
    def __init__(self, account_number, pin, balance=0.0):
        self.account_number = str(account_number)
        self.__pin = str(pin)
        self.balance = float(balance)

    def verify_pin(self, entered_pin):
        return self.__pin == str(entered_pin)

    def get_balance(self):
        return self.balance

    def deposit(self, amount):
        if amount <= 0:
            return "Deposit amount must be greater than zero."
        self.balance += amount
        return f"₹{amount:,.2f} deposited successfully."

    def withdraw(self, amount):
        if amount <= 0:
            return "Withdrawal amount must be greater than zero."
        if amount > self.balance:
            return "Insufficient balance."
        self.balance -= amount
        return f"₹{amount:,.2f} withdrawn successfully."

    def masked_account_number(self):
        if len(self.account_number) <= 4:
            return "*" * len(self.account_number)
        return "*" * (len(self.account_number) - 4) + self.account_number[-4:]
