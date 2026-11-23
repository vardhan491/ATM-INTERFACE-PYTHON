class ATM:
    def __init__(self, account):
        self.account = account

    def authenticate(self):
        print("\n===== Welcome to Python ATM =====")
        for attempt in range(3):
            pin = input("Enter your 4-digit PIN: ").strip()
            if self.account.verify_pin(pin):
                print("\nLogin successful.")
                return True
            remaining = 2 - attempt
            if remaining:
                print(f"Incorrect PIN. {remaining} attempt(s) remaining.")
        print("Too many incorrect attempts. Your session has ended.")
        return False

    def show_menu(self):
        print("\n========== ATM MENU ==========")
        print("1. Check balance")
        print("2. Deposit money")
        print("3. Withdraw money")
        print("4. Account details")
        print("5. Exit")

    def start(self):
        if not self.authenticate():
            return

        while True:
            self.show_menu()
            choice = input("Choose an option (1-5): ").strip()

            if choice == "1":
                print(f"Available balance: ₹{self.account.get_balance():,.2f}")
            elif choice == "2":
                self._handle_transaction("deposit")
            elif choice == "3":
                self._handle_transaction("withdraw")
            elif choice == "4":
                print(f"Account number: {self.account.masked_account_number()}")
            elif choice == "5":
                print("Thank you for using Python ATM. Goodbye!")
                break
            else:
                print("Invalid choice. Please select a number from 1 to 5.")

    def _handle_transaction(self, transaction_type):
        try:
            amount = float(input("Enter amount: ₹").strip())
            if transaction_type == "deposit":
                message = self.account.deposit(amount)
            else:
                message = self.account.withdraw(amount)
            print(message)
        except ValueError:
            print("Please enter a valid numeric amount.")
