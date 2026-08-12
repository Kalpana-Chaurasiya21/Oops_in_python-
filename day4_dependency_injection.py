"""
ADVANCED DESIGN CONCEPTS (PART 2): DEPENDENCY INJECTION

DEFINITION:
Dependency Injection (DI) is a design pattern where an object receives its dependencies from the outside
rather than instantiating them internally.

USES & APPLICATIONS:
1. Decoupling: Easily swap out components (e.g., switching from a Mock Email Logger to a Real Email Logger).
2. Unit Testing: Pass fake/mock dependencies into classes to test them in isolation.
"""


class LoggerService:  # Interface-like base logger dependency
    def log(self, message: str):  # Base logging method
        print(f"[SYSTEM LOG]: {message}")  # Default log output


class DatabaseService:  # Core service requiring a Logger dependency
    def __init__(self, logger: LoggerService):  # Dependency Injection: Logger passed in via constructor
        self.logger = logger  # Injected dependency stored as instance attribute

    def save_data(self, data: str):  # Method performing database work
        # Performs work...
        self.logger.log(f"Successfully saved entry: '{data}' to DB.")  # Uses injected logger dependency


#  EXECUTION & DEMONSTRATION 

external_logger = LoggerService()  # Instantiates dependency externally
db_service = DatabaseService(external_logger)  # Injects dependency into DatabaseService

print("# --- Dependency Injection Output ---")  # Section header
db_service.save_data("User_User101_Record")  # Executes database operation using injected logger