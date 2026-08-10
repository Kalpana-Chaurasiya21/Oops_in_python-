"""
DEFINITIONS:
Polymorphism: The ability of different objects to respond to the same method call in their own specific way.
Compile-Time Polymorphism (Static): Decisions are made before execution. Python achieves this via Method Overloading (simulated using default parameters or *args).
Run-Time Polymorphism (Dynamic): Decisions are made during execution. Python achieves this via Method Overriding (subclasses redefining parent methods) and Duck Typing.

USES & APPLICATIONS:
1. Flexible Functions: Functions can handle default, missing, or variable arguments seamlessly without breaking.
2. Dynamic Behavior: Allows child classes to change inherited logic dynamically at runtime based on the specific object being used.
"""


# --- 1. COMPILE-TIME POLYMORPHISM (Method Overloading Simulation) ---
class Calculator:  # Class demonstrating simulated method overloading
    def add(self, a: float, b: float = 0, c: float = 0) -> float:  # Method with default parameters to handle different call signatures
        return a + b + c  # Computes sum based on provided arguments


# 2. RUN-TIME POLYMORPHISM (Method Overriding) 
class Shape:  # Parent base class for shape objects
    def area(self) -> float:  # Base method interface to be overridden by child classes
        return 0.0  # Default area value


class Square(Shape):  # Child class inheriting from Shape
    def __init__(self, side: float):  # Constructor for Square
        self.side = side  # Stores side length attribute

    def area(self) -> float:  # Overrides parent area method specifically for Square
        return self.side * self.side  # Calculates square area


class Circle(Shape):  # Child class inheriting from Shape
    def __init__(self, radius: float):  # Constructor for Circle
        self.radius = radius  # Stores radius attribute

    def area(self) -> float:  # Overrides parent area method specifically for Circle
        return 3.14159 * self.radius * self.radius  # Calculates circle area


# 3. RUN-TIME POLYMORPHISM (Duck Typing) 
class CustomBox:  # Standalone class not inheriting from Shape
    def area(self) -> float:  # Implements area method matching the same interface signature
        return 100.0  # Returns fixed custom box area


def print_shape_area(shape_object):  # Dynamic function handling any object with an area method
    print(f"Calculated Area: {shape_object.area():.2f}")  # Calls area method polymorphically at runtime


#  EXECUTION & DEMONSTRATION 

calc = Calculator()  # Instantiates Calculator object
print("--- Compile-Time Polymorphism (Method Overloading) ---")  # Section header for overloading
print(f"Add 1 argument: {calc.add(10)}")  # Calls add with 1 parameter (Outputs 10)
print(f"Add 2 arguments: {calc.add(10, 20)}")  # Calls add with 2 parameters (Outputs 30)
print(f"Add 3 arguments: {calc.add(10, 20, 30)}")  # Calls add with 3 parameters (Outputs 60)

square = Square(4.0)  # Instantiates Square object
circle = Circle(3.0)  # Instantiates Circle object
box = CustomBox()  # Instantiates CustomBox object (Duck Typing)

print("\n--- Run-Time Polymorphism (Method Overriding & Duck Typing) ---")  # Section header for runtime polymorphism
print_shape_area(square)  # Resolves area for Square dynamically (Outputs 16.00)
print_shape_area(circle)  # Resolves area for Circle dynamically (Outputs 28.27)
print_shape_area(box)  # Resolves area for CustomBox dynamically via Duck Typing (Outputs 100.00)