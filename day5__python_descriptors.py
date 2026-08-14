"""
ADVANCED MECHANICS (PART 2): PYTHON DESCRIPTORS

DEFINITION:
Descriptors are classes that define custom behavior when accessing, setting, or deleting 
attributes on another class by implementing __get__, __set__, or __delete__.

USES & APPLICATIONS:
Reusable Validation: Enforces attribute rules (e.g., non-negative prices, valid emails) across multiple classes without repeating @property logic.
Framework Internals: Power modern Python ORMs (like Django/SQLAlchemy) to map database columns.
"""


class NonNegativeNumber:  # Descriptor class enforcing non-negative numeric attributes
    def __set_name__(self, owner, name):  # Called automatically at class creation
        self.private_name = "_" + name  # Generates private attribute backing name

    def __get__(self, instance, owner):  # Intercepts attribute read
        if instance is None:  # Accessed from class directly
            return self  # Returns descriptor instance
        return getattr(instance, self.private_name, 0)  # Returns stored value or default 0

    def __set__(self, instance, value):  # Intercepts attribute assignment
        if value < 0:  # Validation rule check
            raise ValueError(f"Invalid Value: '{self.private_name[1:]}' cannot be negative!")  # Rejects invalid input
        setattr(instance, self.private_name, value)  # Stores validated value in private attribute


class Product:  # Class utilizing descriptor validation
    price = NonNegativeNumber()  # Applied to price attribute
    stock = NonNegativeNumber()  # Applied to stock attribute

    def __init__(self, name: str, price: float, stock: int):  # Constructor
        self.name = name  # Public attribute
        self.price = price  # Triggers NonNegativeNumber.__set__
        self.stock = stock  # Triggers NonNegativeNumber.__set__


#  EXECUTION & DEMONSTRATION 

item = Product("Gaming Laptop", 1200.0, 15)  # Instantiates product

print("# --- Descriptors Output ---")  # Section header
print(f"Product: {item.name} | Price: ${item.price} | Stock: {item.stock}")  # Reads validated values

try:  # Tests validation enforcement
    item.price = -500.0  # Attempting negative assignment
except ValueError as e:  # Catches descriptor error
    print(f"Validation Rejected -> {e}")  # Handled error output