"""
TYPES OF ABSTRACTION (PART 1): ABSTRACT BASE CLASSES (ABCs)

DEFINITION:
An Abstract Base Class (ABC) cannot be instantiated directly. It serves as a strict
blueprint requiring child classes to override and implement all @abstractmethod declarations.

DIFFERENCES:
1. Concrete Class: Can be instantiated directly (e.g., obj = ClassName()).
2. Abstract Class: Raises a TypeError if instantiated directly or if child classes fail to implement abstract methods.
"""

from abc import ABC, abstractmethod  # Imports ABC base class and abstractmethod decorator


class PaymentGateway(ABC):  # Abstract Base Class template
    @abstractmethod
    def process_payment(self, amount: float):  # Abstract method requirement
        pass  # Subclasses must implement this exact method signature


class CreditCardGateway(PaymentGateway):  # Child subclass 1
    def process_payment(self, amount: float):  # Implements required abstract method
        print(f"Processing ${amount:.2f} via Credit Card network.")  # Payment execution logic


class PayPalGateway(PaymentGateway):  # Child subclass 2
    def process_payment(self, amount: float):  # Implements required abstract method
        print(f"Processing ${amount:.2f} via PayPal API.")  # Payment execution logic


# --- EXECUTION & DEMONSTRATION ---

card = CreditCardGateway()  # Instantiates concrete CreditCardGateway
paypal = PayPalGateway()  # Instantiates concrete PayPalGateway

print("# --- ABC Enforcement Demonstration Output ---")  # Section header
card.process_payment(100.0)  # Calls credit card implementation
paypal.process_payment(50.0)  # Calls paypal implementation

print("\n# --- Instantiation Protection Test ---")  # Section header
try:  # Testing abstract instantiation restriction
    direct_gateway = PaymentGateway()  # Fails because PaymentGateway is abstract
except TypeError:  # Catches expected exception
    print("Abstraction Protection: Cannot instantiate Abstract Base Class directly!")  # Security confirmation