"""
DEFINITIONS:
Encapsulation: Restricting direct access to an object's internal data and state using private attributes and controlled methods (Getters/Setters).
Abstraction: Hiding complex implementation logic and exposing only a simple, high-level interface to the caller.
Encapsulation vs Abstraction: Encapsulation is about DATA SECURITY (how data is contained and protected), while Abstraction is about HIDING COMPLEXITY (how functionality is simplified).

USES & APPLICATIONS:
1. System Security: Prevents unauthorized external modification of crucial internal variables.
2. Maintainability: Allows developers to change background code or algorithms without breaking code that depends on the interface.
"""

from abc import ABC, abstractmethod  # Imports modules to build abstract class templates


# --- ABSTRACT INTERFACE (Hiding Complexity) ---
class ATMSystem(ABC):  # Abstract Base Class defining the high-level ATM interface
    @abstractmethod
    def withdraw_cash(self, pin: int, amount: float):  # Abstract method signature exposed to users
        pass  # Placeholder requiring subclass implementation


# --- CONCRETE IMPLEMENTATION (Encapsulation + Abstraction) ---
class BankATM(ATMSystem):  # Subclass providing specific ATM logic
    def __init__(self, account_holder: str, initial_balance: float, correct_pin: int):  # Constructor
        self.account_holder = account_holder  # Public attribute (identifies the user)
        self.__balance = initial_balance  # Private attribute (Encapsulation: protected balance)
        self.__pin = correct_pin  # Private attribute (Encapsulation: protected PIN code)

    # --- PRIVATE HELPER METHODS (Internal Complexity Hidden via Abstraction) ---
    def __verify_pin(self, entered_pin: int) -> bool:  # Private method to validate security PIN
        return self.__pin == entered_pin  # Returns True if PIN matches internal private PIN

    def __has_sufficient_cash(self, amount: float) -> bool:  # Private method checking funds
        return self.__balance >= amount  # Returns True if current balance can cover request

    # --- PUBLIC INTERFACE METHOD (Exposing Simple Operations) ---
    def withdraw_cash(self, pin: int, amount: float):  # Main operational method
        if not self.__verify_pin(pin):  # Calls hidden private PIN validation check
            print("Access Denied: Incorrect PIN!")  # Rejects transaction on bad PIN
            return  # Exits method

        if not self.__has_sufficient_cash(amount):  # Calls hidden private balance check
            print(f"Transaction Failed: Insufficient funds. Current Balance: ${self.__balance:.2f}")  # Rejects overdraft
            return  # Exits method

        self.__balance -= amount  # Safely updates internal private balance state
        print(f"Transaction Successful: Dispensed ${amount:.2f}. Remaining Balance: ${self.__balance:.2f}")  # Success output


# --- EXECUTION & DEMONSTRATION ---

atm = BankATM("John Doe", 1000.0, 4321)  # Instantiates BankATM with $1000 balance and PIN 4321

print("--- Testing Abstraction (Simple Interface Call) ---")  # Section header for abstraction
atm.withdraw_cash(4321, 200.0)  # Caller just provides PIN and amount without seeing background checks

print("\n--- Testing Protection (Encapsulation Checks) ---")  # Section header for encapsulation
atm.withdraw_cash(9999, 100.0)  # Fails PIN verification safely without exposing system internals
atm.withdraw_cash(4321, 2000.0)  # Fails overdraft check safely without exposing raw balance variable

print("\n--- Direct Data Access Security Test ---")  # Section header for direct variable access
try:  # Uses try block to test direct variable modification
    print(atm.__balance)  # Attempts direct read of encapsulated balance
except AttributeError:  # Catches AttributeError thrown by Python privacy protection
    print("Encapsulation Success: Internal balance cannot be directly read or modified!")  # Confirms encapsulatio