# SOLID Principles 
# I - Interface Segregation Principle (ISP): Don't force classes to implement methods they don't use.
# D - Dependency Inversion Principle (DIP): High-level modules shouldn't depend on low-level modules; both should depend on abstractions.

from abc import ABC, abstractmethod


# INTERFACE SEGREGATION PRINCIPLE (ISP) 
# Instead of one fat 'Worker' interface with work(), eat(), and sleep(), break them up.

class Workable(ABC):
    @abstractmethod
    def work(self):
        pass


class Eatable(ABC):
    @abstractmethod
    def eat(self):
        pass


class HumanWorker(Workable, Eatable):
    def work(self):
        print("Human working on code...")

    def eat(self):
        print("Human taking a lunch break...")


class RobotWorker(Workable):
    # Robots don't eat! So they only implement Workable.
    def work(self):
        print("Robot assembling parts 24/7...")


# --- 2. DEPENDENCY INVERSION PRINCIPLE (DIP) ---
# High-level NotificationService depends on abstract MessageSender, not concrete Email/SMS classes.

class MessageSender(ABC):
    @abstractmethod
    def send(self, recipient: str, message: str):
        pass


class EmailSender(MessageSender):
    def send(self, recipient: str, message: str):
        print(f"[Email to {recipient}]: {message}")


class SMSSender(MessageSender):
    def send(self, recipient: str, message: str):
        print(f"[SMS to {recipient}]: {message}")


class NotificationService:
    def __init__(self, sender: MessageSender):  # Injected abstraction dependency
        self.sender = sender

    def notify(self, user: str, msg: str):
        self.sender.send(user, msg)


#  Example Usage 

print("# --- ISP & DIP Demonstration ---")

# ISP Check
robot = RobotWorker()
robot.work()

# DIP Check
email_notifier = NotificationService(EmailSender())
email_notifier.notify("alex@example.com", "System maintenance at midnight.")

sms_notifier = NotificationService(SMSSender())
sms_notifier.notify("+123456789", "Your OTP code is 4829.")