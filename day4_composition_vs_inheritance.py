"""
DAY 5 CORE CONCEPT: COMPOSITION VS INHERITANCE

DEFINITIONS:
Inheritance (Is-A Relationship): A class inherits from a parent class (e.g., A Dog IS-A Animal).
Composition (Has-A Relationship): A class contains instances of other classes as attributes (e.g., A Car HAS-AN Engine).

USES & APPLICATIONS:
1. "Favor Composition over Inheritance": Prevents deep, brittle inheritance hierarchies.
2. Flexibility: Allows changing component behaviors dynamically at runtime.
"""


#  COMPONENT CLASS 
class Engine:  # Independent class representing an Engine component
    def __init__(self, horsepower: int):  # Constructor
        self.horsepower = horsepower  # Stores horsepower rating

    def start(self):  # Engine operational method
        print(f"Engine with {self.horsepower} HP roars to life! 🏎️")  # Output message


#  COMPOSITE CLASS (HAS-A RELATIONSHIP) 
class Car:  # Car class using Composition instead of inheriting from Engine
    def __init__(self, brand: str, horsepower: int):  # Constructor
        self.brand = brand  # Car attribute
        self.engine = Engine(horsepower)  # Composition: Car HAS-AN Engine instance inside it

    def drive(self):  # Operational method delegating work to component
        print(f"Driving the {self.brand}...")  # Output message
        self.engine.start()  # Delegates engine start logic to internal Engine object


#  EXECUTION & DEMONSTRATION 

my_car = Car("Ford Mustang", 450)  # Instantiates Car object containing an Engine

print("# --- Composition Core Demonstration Output ---")  # Section header
my_car.drive()  # Triggers car driving logic and internal engine execution