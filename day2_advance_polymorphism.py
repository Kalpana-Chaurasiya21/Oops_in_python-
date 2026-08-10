"""
DEFINITIONS:
Operator Overloading: Customizing the behavior of built-in operators (+, -, *, ==) for user-defined class objects using magic (dunder) methods.
Polymorphic Abstract Interfaces: Using Abstract Base Classes to enforce that different subclasses share identical polymorphic method signatures.

USES & APPLICATIONS:
1. Intuitive Syntax: Allows custom objects to be added, compared, or printed using native Python operators like '+' or '=='.
2. API Design & Security: Forces team members to follow uniform method signatures across different object implementations.
"""

from abc import ABC, abstractmethod  # Imports Abstract Base Class modules


# --- 1. OPERATOR OVERLOADING (Polymorphism with Native Operators) ---
class Vector:  # Class representing a 2D mathematical vector
    def __init__(self, x: float, y: float):  # Constructor setting x and y coordinates
        self.x = x  # Stores x coordinate attribute
        self.y = y  # Stores y coordinate attribute

    def __add__(self, other):  # Overloads the '+' operator polymorphically
        return Vector(self.x + other.x, self.y + other.y)  # Returns a new Vector instance with summed coordinates

    def __eq__(self, other) -> bool:  # Overloads the '==' operator polymorphically
        return self.x == other.x and self.y == other.y  # Returns True if coordinates match, otherwise False

    def __str__(self) -> str:  # Overloads string conversion (used by print)
        return f"Vector({self.x}, {self.y})"  # Formats object representation as string


# --- 2. POLYMORPHIC ABSTRACT INTERFACE ---
class NotificationSender(ABC):  # Abstract base interface
    @abstractmethod
    def send(self, message: str):  # Abstract method signature
        pass  # Placeholder requiring subclass implementation


class EmailNotification(NotificationSender):  # Subclass 1 implementing interface
    def send(self, message: str):  # Implements send specifically for Email
        print(f"Sending Email: {message}")  # Email dispatch logic


class SMSNotification(NotificationSender):  # Subclass 2 implementing interface
    def send(self, message: str):  # Implements send specifically for SMS
        print(f"Sending SMS: {message}")  # SMS dispatch logic


def notify_user(sender: NotificationSender, text: str):  # Polymorphic dispatcher function
    sender.send(text)  # Dispatches message polymorphically regardless of notification transport


# --- EXECUTION & DEMONSTRATION ---

v1 = Vector(2, 4)  # Instantiates first Vector object
v2 = Vector(3, 1)  # Instantiates second Vector object

print("--- Operator Overloading Output ---")  # Section header for operator overloading
v3 = v1 + v2  # Uses overloaded '+' operator (calls v1.__add__(v2))
print(f"v1 + v2 = {v3}")  # Prints formatted sum vector (Outputs: Vector(5, 5))
print(f"Is v1 equal to v2? {v1 == v2}")  # Uses overloaded '==' operator (Outputs: False)

email = EmailNotification()  # Instantiates EmailNotification object
sms = SMSNotification()  # Instantiates SMSNotification object

print("\n--- Abstract Interface Polymorphism Output ---")  # Section header for interface polymorphism
notify_user(email, "Your order has shipped!")  # Triggers polymorphic email send
notify_user(sms, "Your security code is 4920.")  # Triggers polymorphic SMS send