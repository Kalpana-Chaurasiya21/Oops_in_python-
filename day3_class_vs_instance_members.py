"""
DEFINITIONS:
Class Attributes/Methods: Shared across ALL instances of a class. Stored once in memory.
Instance Attributes/Methods: Unique to EACH individual instance/object created from the class.
Static Methods: Utility functions attached to a class namespace that do not access class (cls) or instance (self) state.

USES & APPLICATIONS:
1. Shared Counters: Track global statistics (e.g., total registered users across an entire system).
2. Factory Methods: Use @classmethod to create objects from alternative data formats (e.g., parsing JSON or strings).
3. Utility Functions: Use @staticmethod to organize pure functions inside relevant classes without instantiating objects.
"""


class Employee:  # Base class demonstrating member types
    company_name = "Tech Corp"  # Class Attribute: Shared by all Employee instances
    total_employees = 0  # Class Attribute: Keeps global count of created employees

    def __init__(self, name: str, salary: float):  # Constructor method
        self.name = name  # Instance Attribute: Unique to each individual employee
        self.salary = salary  # Instance Attribute: Unique salary value
        Employee.total_employees += 1  # Updates shared class variable upon object creation

    def get_details(self) -> str:  # Instance Method: Uses 'self' to access specific instance data
        return f"Employee: {self.name} | Salary: ${self.salary:.2f} | Company: {self.company_name}"

    @classmethod
    def get_company_stats(cls) -> str:  # Class Method: Uses 'cls' to access/modify class-level state
        return f"Company: {cls.company_name} | Total Headcount: {cls.total_employees}"

    @classmethod
    def from_string(cls, emp_str: str):  # Class Method used as an alternative constructor (Factory Method)
        name, salary = emp_str.split("-")  # Parses formatted string "Name-Salary"
        return cls(name, float(salary))  # Instantiates and returns new Employee object

    @staticmethod
    def is_valid_salary(salary: float) -> bool:  # Static Method: Independent utility function
        return salary >= 30000.0  # Returns True if salary meets minimum threshold


# --- EXECUTION & DEMONSTRATION ---

emp1 = Employee("Alice", 75000.0)  # Standard instantiation using __init__
emp2 = Employee.from_string("Bob-50000")  # Factory instantiation using @classmethod

print("--- Instance Methods & Attributes Output ---")  # Section header for instance members
print(emp1.get_details())  # Displays Alice's details using self
print(emp2.get_details())  # Displays Bob's details using self

print("\n--- Class Methods & Shared State Output ---")  # Section header for class members
print(Employee.get_company_stats())  # Displays shared headcount (Outputs 2)

print("\n--- Static Method Utility Output ---")  # Section header for static methods
print(f"Is $25,000 valid? {Employee.is_valid_salary(25000.0)}")  # Tests static method (Outputs False)
print(f"Is $50,000 valid? {Employee.is_valid_salary(50000.0)}")  # Tests static method (Outputs True)