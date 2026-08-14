"""
ADVANCED MECHANICS (PART 1): CUSTOM CONTEXT MANAGERS

DEFINITIONS:
Context Manager: A class that manages resources cleanly using Python's 'with' statement.
They utilize special dunder methods __enter__ and __exit__ to automate setup and teardown.

USES & APPLICATIONS:
 Automated Cleanup: Guarantees files, database sockets, or locks close safely even if errors occur.
 Exception Handling: Option to intercept, log, or suppress runtime exceptions cleanly.
"""


class ManagedFile:  # Custom Context Manager class
    def __init__(self, filename: str, mode: str):  # Constructor
        self.filename = filename  # Target file path
        self.mode = mode  # Opening mode ('r', 'w', etc.)
        self.file = None  # Resource handle placeholder

    def __enter__(self):  # Triggers when entering the 'with' block
        print(f"Opening file '{self.filename}' safely...")  # Setup message
        self.file = open(self.filename, self.mode)  # Opens target file
        return self.file  # Returns file handle to 'with ... as' variable

    def __exit__(self, exc_type, exc_val, exc_tb):  # Triggers when leaving 'with' block
        if self.file:  # Checks if resource handle exists
            self.file.close()  # Closes file handle safely
        print(f"Closed file '{self.filename}' cleanly.")  # Teardown message
        if exc_type:  # Checks if an exception occurred inside the block
            print(f"Handled Exception inside block: {exc_val}")  # Intercepts exception
        return True  # Suppresses exception from crashing the program


# EXECUTION & DEMONSTRATION 

print("# --- Context Manager Output ---")  # Section header
with ManagedFile("test_log.txt", "w") as f:  # Enters context block
    f.write("Logging OOP Day 6 Execution...")  # Writes data
    print("Writing contents to file inside 'with' block.")  # Status update
# Automatically triggers __exit__ when leaving block