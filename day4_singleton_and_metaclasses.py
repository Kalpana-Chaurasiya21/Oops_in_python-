"""
DAY 6 CORE CONCEPT: SINGLETON PATTERN & METACLASSES

DEFINITIONS:
Singleton Pattern: A design pattern that restricts the instantiation of a class to ONE single object instance across the entire application.
Metaclass: A "class of a class" that defines how a class itself is constructed and behaves.

USES & APPLICATIONS:
1. Shared Resources: Ideal for global resource managers like Database Connection Pools or Logging Services.
2. Centralized State: Ensures all parts of an application share the exact same configuration instance.
"""


class SingletonMeta(type):  # Metaclass inheriting from built-in 'type'
    _instances = {}  # Dictionary storing single instances of classes

    def __call__(cls, *args, **kwargs):  # Triggered when a class instance is created
        if cls not in cls._instances:  # Checks if class instance exists already
            instance = super().__call__(*args, **kwargs)  # Creates instance via base type
            cls._instances[cls] = instance  # Caches created instance in dictionary
        return cls._instances[cls]  # Returns cached single instance


class DatabaseConnection(metaclass=SingletonMeta):  # Class enforcing Singleton via SingletonMeta
    def __init__(self, db_url: str):  # Constructor
        self.db_url = db_url  # Database URL attribute

    def connect(self):  # Operational method
        print(f"Connected to Database at: {self.db_url}")  # Output message


# --- EXECUTION & DEMONSTRATION ---

db1 = DatabaseConnection("localhost:5432/production")  # First instantiation call
db2 = DatabaseConnection("localhost:5432/staging")  # Second instantiation call

print("# --- Singleton Pattern Demonstration Output ---")  # Section header
print(f"db1 Memory ID: {id(db1)}")  # Memory address of db1
print(f"db2 Memory ID: {id(db2)}")  # Memory address of db2
print(f"Are db1 and db2 the exact same instance? {db1 is db2}")  # Evaluates to True