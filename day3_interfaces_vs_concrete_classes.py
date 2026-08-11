"""
TYPES OF ABSTRACTION (PART 2): INFORMAL INTERFACES vs CONCRETE CLASSES

DEFINITIONS:
Interface: A pure contract containing ONLY abstract methods with zero implementation code.
Concrete Class: A fully defined class providing complete logic for every method, ready to instantiate.

DIFFERENCES:
1. Interface defines WHAT a class must do, but provides NO code execution.
2. Concrete Class defines HOW a class performs its tasks with complete working code.
"""

from abc import ABC, abstractmethod  # Imports ABC modules


# --- PURE INTERFACE ---
class CloudStorageInterface(ABC):  # Pure interface contract
    @abstractmethod
    def upload_file(self, filename: str):  # Method signature requirement 1
        pass  # Pure contract (no code)

    @abstractmethod
    def download_file(self, filename: str):  # Method signature requirement 2
        pass  # Pure contract (no code)


# --- CONCRETE IMPLEMENTATION CLASS ---
class AWSCloudStorage(CloudStorageInterface):  # Concrete class implementing full interface
    def upload_file(self, filename: str):  # Concrete implementation of upload
        print(f"Uploading '{filename}' to Amazon S3 bucket...")  # Implementation logic

    def download_file(self, filename: str):  # Concrete implementation of download
        print(f"Downloading '{filename}' from Amazon S3 bucket...")  # Implementation logic


# --- EXECUTION & DEMONSTRATION ---

storage = AWSCloudStorage()  # Instantiates concrete AWS storage object

print("# --- Interface Implementation Output ---")  # Section header
storage.upload_file("data.csv")  # Invokes concrete upload_file method
storage.download_file("data.csv")  # Invokes concrete download_file method