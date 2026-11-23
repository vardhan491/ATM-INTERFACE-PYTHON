from atm import ATM
from bank_account import BankAccount


def main():
    # Demo account
    account = BankAccount(account_number="1234567890", pin="1234", balance=5000)
    atm = ATM(account)
    atm.start()


if __name__ == "__main__":
    main()
