# A metaclass is basically a class's class.
# Regular classes make instances (objects), but metaclasses make classes.
# You use them when you want to enforce rules across classes before any object is created.

class EnforceNamingMeta(type):
    """
    Metaclass that enforces custom naming rules on class attributes.
    If a developer tries to define a class with non-snake_case attributes,
    this metaclass throws an error when Python loads the module.
    """
    def __new__(mcs, name, bases, attrs):
        # Inspect all defined methods/attributes in the class body
        for key in attrs:
            # Skip internal dunder methods like __init__
            if not key.startswith("__"):
                if not key.islower():
                    raise TypeError(
                        f"Coding Standard Violation: '{key}' in class '{name}' "
                        f"must be written in lowercase (snake_case)!"
                    )
        
        # Everything looks good, construct the class object
        return super().__new__(mcs, name, bases, attrs)


#  Example Usage 

print("# --- Metaclasses Demonstration ---")

# Apply the metaclass using the metaclass keyword in class declaration
class APIClient(metaclass=EnforceNamingMeta):
    user_endpoint = "/api/v1/users"  # Passes check
    
    def fetch_data(self):  # Passes check
        print("Fetching data from API...")


client = APIClient()
client.fetch_data()

print("APIClient class passed all naming checks successfully.")

# Testing Enforcement: Uncommenting the code below will crash on startup
# class BadClient(metaclass=EnforceNamingMeta):
#     UserEndpoint = "/api/v1/users"  # Throws TypeError for CamelCase!