"""
TYPES OF INHERITANCE (PART 2):

DEFINITIONS:
Multilevel Inheritance: A child class inherits from a parent class, which itself inherits from a grandparent class (chain).
Hierarchical Inheritance: MULTIPLE child classes inherit from the SAME single parent class.

DIFFERENCES:
1. Structure: Multilevel forms a vertical chain (A -> B -> C); Hierarchical forms a tree branching out (A -> B and A -> C).
2. Data Sharing: Multilevel passes properties down a linear chain; Hierarchical shares base properties horizontally across siblings.
"""


# --- 1. MULTILEVEL INHERITANCE ---
class Device:  # Grandparent base class
    def power_on(self):  # Grandparent method
        print("Device powered on.")  # Action message


class Computer(Device):  # Parent class inheriting from Device
    def boot_os(self):  # Parent method
        print("Operating System loaded.")  # Action message


class Laptop(Computer):  # Child class inheriting from Computer (and transitively Device)
    def fold(self):  # Child method
        print("Laptop screen folded.")  # Action message


# --- 2. HIERARCHICAL INHERITANCE ---
class Employee:  # Shared parent class
    def work(self):  # Shared parent method
        print("Employee is performing daily tasks.")  # Action message


class Developer(Employee):  # First sibling child class
    def write_code(self):  # Specific child method
        print("Developer is writing Python code.")  # Action message


class Designer(Employee):  # Second sibling child class inheriting from SAME parent
    def create_ui(self):  # Specific child method
        print("Designer is creating UI mockups.")  # Action message


# --- EXECUTION & DEMONSTRATION ---

print("# --- Multilevel Inheritance Output ---")  # Section header
my_laptop = Laptop()  # Instantiates Laptop
my_laptop.power_on()  # Inherited from Grandparent (Device)
my_laptop.boot_os()  # Inherited from Parent (Computer)
my_laptop.fold()  # Defined in Child (Laptop)

print("\n# --- Hierarchical Inheritance Output ---")  # Section header
dev = Developer()  # Instantiates Developer sibling
des = Designer()  # Instantiates Designer sibling
dev.work()  # Shared method from Employee
dev.write_code()  # Developer specific method
des.work()  # Shared method from Employee
des.create_ui()  # Designer specific method