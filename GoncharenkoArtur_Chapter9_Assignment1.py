class BankAcct:
    # Initializes a bank account with my name, account number, initial amount, and interest rate
    def __init__(self, name, account_number, amount=0.0, interest_rate=0.02):
        self.name = name
        self.account_number = account_number
        self.amount = amount
        self.interest_rate = interest_rate

    # Deposits money into the account
    def deposit(self, amount): 
        if amount > 0:
            self.amount += amount
            print(f"Deposited ${amount:.2f}. New balance: ${self.amount:.2f}")
        else:
            print("Deposit must be positive.")

    # Withdraws the money from the account if sufficient balance is available
    def withdraw(self, amount):
        if 0 < amount <= self.amount:
            self.amount -= amount
            print(f"Withdrew ${amount:.2f}. New balance: ${self.amount:.2f}")
        elif amount > self.amount:
            print("Insufficient funds for withdrawal.")
        else:
            print("Withdrawal amount must be positive.")

    # Adjusts the interest rate
    def adjust_interest_rate(self, new_rate):
        if new_rate >= 0:
            self.interest_rate = new_rate
            print(f"New interest rate set to {self.interest_rate:.2%}")
        else:
            print("Interest rate can't be negative.")

    # Calculates the interest earned over a given number of days
    def calculate_interest(self, days):
        if days < 0:
            print("Number of days can't be negative.")
            return 0
        daily_rate = self.interest_rate / 365
        interest_earned = self.amount * daily_rate * days
        return interest_earned

    def get_balance(self):
        return self.amount

    def __str__(self):
        return f"Account: {self.account_number}, Name: {self.name}, Balance: ${self.amount:.2f}, Interest Rate: {self.interest_rate:.2%}"


def test_bank_account():
    # Creates a new bank account
    account = BankAcct("Artur Goncharenko", "5000", 6000, 0.07)

    print("\n--- Initial Account Details ---")
    print(account)

    # Tests the deposit
    account.deposit(500)

    # Testz the withdrawal
    account.withdraw(200)
    account.withdraw(2000) 

    # Tests interest calculation
    interest_30_days = account.calculate_interest(30)
    print(f"Interest earned in 30 days: ${interest_30_days:.2f}")

    # Tests adjusting interest rate
    account.adjust_interest_rate(0.04)

    # Tests interest calculation after rate change
    interest_30_days_new_rate = account.calculate_interest(30)
    print(f"Interest earned in 30 days with new rate: ${interest_30_days_new_rate:.2f}")

    # Displays the final account details
    print("\n--- Final Account Details ---")
    print(account)

# Runs the test function
test_bank_account()
