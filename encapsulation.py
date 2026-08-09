class BankAccount:  # Defines the BankAccount blueprint class
    def __init__(self, account_holder: str, initial_balance: float):  # Constructor method to set up account attributes
        self.account_holder = account_holder  # Public attribute: accessible directly anywhere
        self.__balance = initial_balance  # Private attribute: prefix '__' hides it from direct external access

    def get_balance(self) -> float:  # Getter method: safely provides read-only access to __balance
        return self.__balance  # Returns current private balance value

    def deposit(self, amount: float):  # Setter method: safely updates __balance with input validation
        if amount > 0:  # Validates that deposit amount is positive
            self.__balance += amount  # Adds amount to private balance
            print(f"Deposited ${amount:.2f}. New balance: ${self.__balance:.2f}")  # Displays success message
        else:  # Handles invalid deposit attempts
            print("Deposit error: Amount must be greater than 0.")  # Displays error message

    def withdraw(self, amount: float):  # Setter method: validates and reduces __balance
        if amount <= 0:  # Validates that withdrawal amount is positive
            print("Withdrawal error: Amount must be greater than 0.")  # Displays error for invalid amount
        elif amount > self.__balance:  # Checks if withdrawal amount exceeds current balance
            print(f"Withdrawal error: Insufficient funds. Available: ${self.__balance:.2f}")  # Displays overdraft warning
        else:  # Executes withdrawal when funds are sufficient
            self.__balance -= amount  # Subtracts amount from private balance
            print(f"Withdrew ${amount:.2f}. Remaining balance: ${self.__balance:.2f}")  # Displays success message


account1 = BankAccount("Alice", 500.0)  # Instantiates account1 object with holder "Alice" and balance 500.0
print(f"Account Holder: {account1.account_holder}")  # Directly reads public attribute account_holder
print(f"Initial Balance: ${account1.get_balance():.2f}")  # Reads private __balance safely using getter method

account1.deposit(200.0)  # Calls deposit method with valid positive amount (Balance becomes 700.0)
account1.withdraw(150.0)  # Calls withdraw method with valid amount (Balance becomes 550.0)

account1.deposit(-50.0)  # Tests validation check by attempting negative deposit
account1.withdraw(1000.0)  # Tests validation check by attempting overdraft withdrawal

try:  # Uses try block to catch expected access error
    print(account1.__balance)  # Attempts direct access to private attribute (raises AttributeError)
except AttributeError:  # Catches AttributeError thrown by Python's privacy protection
    print("Security Check: Cannot access '__balance' directly outside the class.")  # Confirms encapsulation works