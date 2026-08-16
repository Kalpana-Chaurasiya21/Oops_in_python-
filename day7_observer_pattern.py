# Observer Pattern
# Defines a subscription mechanism to notify multiple objects (observers)
# about any events that happen to the object they're listening to (subject).

from abc import ABC, abstractmethod


#  Observer Interface 
class EventObserver(ABC):
    @abstractmethod
    def update(self, event_name: str, data: dict):
        pass


#  Concrete Observers 
class EmailNotifier(EventObserver):
    def update(self, event_name: str, data: dict):
        if event_name == "user_registered":
            print(f"[Email Service] Sending welcome email to {data.get('email')}")


class AnalyticsTracker(EventObserver):
    def update(self, event_name: str, data: dict):
        print(f"[Analytics] Logged event '{event_name}' for user ID {data.get('user_id')}")


class AuditLogger(EventObserver):
    def update(self, event_name: str, data: dict):
        print(f"[Audit Log] Security event record created for '{event_name}'")


#  Subject / Publisher 
class UserManager:
    def __init__(self):
        self._observers = []

    def attach(self, observer: EventObserver):
        if observer not in self._observers:
            self._observers.append(observer)

    def detach(self, observer: EventObserver):
        self._observers.remove(observer)

    def notify(self, event_name: str, data: dict):
        for observer in self._observers:
            observer.update(event_name, data)

    def register_user(self, user_id: int, username: str, email: str):
        print(f"\n--> Registering new user: {username}")
        # Core user registration logic here...
        user_data = {"user_id": user_id, "username": username, "email": email}
        
        # Publish event to all subscribed listeners
        self.notify("user_registered", user_data)


#  Example Usage 

print("# --- Observer Pattern Demonstration ---")

user_service = UserManager()

# Register observers
email_service = EmailNotifier()
analytics = AnalyticsTracker()
audit = AuditLogger()

user_service.attach(email_service)
user_service.attach(analytics)
user_service.attach(audit)

# Trigger event
user_service.register_user(101, "sarah_k", "sarah@example.com")

# Unsubscribe audit logger and run another registration
user_service.detach(audit)
user_service.register_user(102, "mark_d", "mark@example.com")