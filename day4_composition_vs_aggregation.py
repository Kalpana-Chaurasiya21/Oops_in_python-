"""
ADVANCED DESIGN CONCEPTS (PART 1): COMPOSITION VS AGGREGATION

DEFINITIONS:
Composition (Strong Ownership): The child object CANNOT exist without the parent object (e.g., House and Room). If the parent is destroyed, the child is destroyed.
Aggregation (Weak Ownership): The child object CAN exist independently of the parent object (e.g., Department and Teacher).

DIFFERENCES:
1. Lifecycle Dependency: In Composition, child life is tightly bound to parent. In Aggregation, child lives independently.
2. Object Passing: Aggregation passes external existing objects into the class; Composition creates child objects internally.
"""


#  AGGREGATION EXAMPLE (Independent Existence) 
class Teacher:  # Standalone teacher class
    def __init__(self, name: str):  # Constructor
        self.name = name  # Teacher name attribute


class Department:  # Parent class aggregating Teachers
    def __init__(self, name: str, teacher: Teacher):  # Accepts external existing Teacher object
        self.name = name  # Department name
        self.teacher = teacher  # Aggregation: Teacher exists independently outside Department


#  COMPOSITION EXAMPLE (Dependent Existence) 
class Room:  # Room class owned by House
    def __init__(self, room_type: str):  # Constructor
        self.room_type = room_type  # Room type attribute


class House:  # Parent class owning Rooms
    def __init__(self):  # Constructor
        self.bedroom = Room("Master Bedroom")  # Composition: Room is instantiated inside House


#  EXECUTION & DEMONSTRATION 

# 1. Aggregation Demonstration
teacher_obj = Teacher("Prof. Smith")  # Teacher created independently
dept = Department("Computer Science", teacher_obj)  # Passed into Department
print("# --- Aggregation Output ---")  # Section header
print(f"Department: {dept.name} | Teacher: {dept.teacher.name}")  # Both exist fine

# 2. Composition Demonstration
my_house = House()  # House creates its own Room
print("\n# --- Composition Output ---")  # Section header
print(f"House contains: {my_house.bedroom.room_type}")  # Room lifetime is bound to House