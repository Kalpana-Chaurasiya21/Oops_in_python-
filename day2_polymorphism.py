"""
DEFINITIONS:
Polymorphism: The ability of different objects to respond to the same method call in their own specific way.
Method Overriding: A child class provides its own implementation of a method that is already defined in its parent class.
Duck Typing: Python's dynamic approach where an object's suitability is determined by the presence of certain methods, not its explicit class inheritance.

USES & APPLICATIONS:
1. Reusability: Write a single function or loop that can process many different object types without changing code.
2. Extensibility: Add new classes in the future without modifying existing functions that use them.
3. Clean Architecture: Replaces messy if-else or type-checking statements with standard method calls.
"""


class PaymentProcessor:  # Parent base class representing generic payment handling
    def process_payment(self, amount: float):  # Base method interface to be overridden by subclasses
        print(f"Processing generic payment of ${amount:.2f}")  # Default implementation message


class CreditCardPayment(PaymentProcessor):  # Child class inheriting from PaymentProcessor
    def process_payment(self, amount: float):  # Overrides parent method specifically for Credit Cards
        print(f"Processing Credit Card payment of ${amount:.2f} via Payment Gateway.")  # Specific logic for Credit Card


class PayPalPayment(PaymentProcessor):  # Child class inheriting from PaymentProcessor
    def process_payment(self, amount: float):  # Overrides parent method specifically for PayPal
        print(f"Processing PayPal payment of ${amount:.2f} via PayPal API.")  # Specific logic for PayPal


class CryptoPayment:  # Standalone class demonstrating Duck Typing (no inheritance from PaymentProcessor)
    def process_payment(self, amount: float):  # Implements process_payment matching the same method signature
        print(f"Processing Crypto payment of ${amount:.2f} via Blockchain transaction.")  # Specific logic for Crypto


def execute_checkout(payment_method, amount: float):  # Polymorphic function handling any payment type
    payment_method.process_payment(amount)  # Calls process_payment dynamically regardless of object class


# --- REAL-WORLD EXAMPLE EXECUTION ---

card_payment = CreditCardPayment()  # Instantiates CreditCardPayment object
paypal_payment = PayPalPayment()  # Instantiates PayPalPayment object
crypto_payment = CryptoPayment()  # Instantiates CryptoPayment object (Duck Typing)

print("--- Polymorphic Checkout Demonstrations ---")  # Section header for checkout calls
execute_checkout(card_payment, 100.50)  # Calls checkout using Credit Card object (Outputs Credit Card message)
execute_checkout(paypal_payment, 45.00)  # Calls checkout using PayPal object (Outputs PayPal message)
execute_checkout(crypto_payment, 250.75)  # Calls checkout using Crypto object (Outputs Blockchain message)

print("\n--- Iterating Through Multiple Payment Methods ---")  # Section header for list processing
transactions = [CreditCardPayment(), PayPalPayment(), CryptoPayment()]  # List containing diverse payment objects
for transaction in transactions:  # Loops through each payment object in the list
    transaction.process_payment(50.00)  # Processes each payment polymorphically using same method call