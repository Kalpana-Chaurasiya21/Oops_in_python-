# Step 1: Define the class blueprint
class Student:
    
    # Step 2: Define the constructor method. 
    # __init__ automatically runs whenever a new Student object is created.
    # 'self' refers to the specific instance of the object being created.
    def __init__(self, name: str, roll_number: int, marks: float):
        # Assign the incoming parameters to the object's own attributes
        self.name = name                 # Stores the student's name
        self.roll_number = roll_number   # Stores the unique roll number
        self.marks = marks               # Stores the student's marks

    # Step 3: Define a method to display student information
    def display_info(self):
        # Access the object's attributes using self.attribute_name
        print(f"Student: {self.name} | Roll No: {self.roll_number} | Marks: {self.marks}")

    # Step 4: Define a method with a conditional check to see if the student passed
    def has_passed(self) -> bool:
        # Returns True if marks are greater than or equal to 40, otherwise returns False
        return self.marks >= 40.0


# Step 5: Create (instantiate) individual Student objects using the class blueprint
student1 = Student("Alice", 101, 85.5)  # Creates student1 with name="Alice", roll_number=101, marks=85.5
student2 = Student("Bob", 102, 32.0)    # Creates student2 with name="Bob", roll_number=102, marks=32.0


# Step 6: Call methods on student1
print("--- Student 1 Info ---")
student1.display_info()                  # Prints Alice's details
print(f"Passed: {student1.has_passed()}") # Output: Passed: True


# Step 7: Call methods on student2
print("\n--- Student 2 Info ---")
student2.display_info()                  # Prints Bob's details
print(f"Passed: {student2.has_passed()}") # Output: Passed: False
