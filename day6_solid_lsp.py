# Liskov Substitution Principle (LSP): 
# Subclasses should be substitutable for their base classes without breaking the system.
# Classic violation: Making a Square inherit from Rectangle, which breaks length/width assumptions.

from abc import ABC, abstractmethod


# BAD EXAMPLE (Violates LSP):
# If Square inherits from Rectangle and overrides width/height setters to change both,
# functions expecting a regular Rectangle will break unexpectedly.


# CORRECT APPROACH: Separate into proper abstraction abstractions.

class Shape(ABC):
    @abstractmethod
    def calculate_area(self) -> float:
        pass


class Rectangle(Shape):
    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height

    def calculate_area(self) -> float:
        return self.width * self.height


class Square(Shape):
    def __init__(self, side: float):
        self.side = side

    def calculate_area(self) -> float:
        return self.side ** 2


def print_area(shape: Shape):
    """Works safely with ANY Shape subclass without making wrong assumptions."""
    print(f"Area of {shape.__class__.__name__}: {shape.calculate_area()}")


# Example Usage 

print("# --- Liskov Substitution Principle Demonstration ---")

rect = Rectangle(10, 5)
sq = Square(4)

print_area(rect)
print_area(sq)