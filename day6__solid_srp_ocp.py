# SOLID Principles 
# S - Single Responsibility Principle (SRP): A class should have one, and only one, reason to change.
# O - Open/Closed Principle (OCP): Code should be open for extension, but closed for modification.

from abc import ABC, abstractmethod


#  SINGLE RESPONSIBILITY PRINCIPLE (SRP) 
# Instead of one massive class handling data, formatting, and saving, we split them.

class Invoice:
    """Handles only business logic related to the order data."""
    def __init__(self, customer: str, amount: float):
        self.customer = customer
        self.amount = amount


class InvoiceRepository:
    """Handles only database/storage persistence."""
    def save(self, invoice: Invoice):
        print(f"[DB] Saving invoice for {invoice.customer} (${invoice.amount:.2f}) to database...")


# --- 2. OPEN/CLOSED PRINCIPLE (OCP) ---
# We use interfaces/ABCs so we can add new discount types without touching existing code.

class DiscountStrategy(ABC):
    @abstractmethod
    def apply_discount(self, amount: float) -> float:
        pass


class StandardDiscount(DiscountStrategy):
    def apply_discount(self, amount: float) -> float:
        return amount * 0.90  # 10% off


class VIPDiscount(DiscountStrategy):
    def apply_discount(self, amount: float) -> float:
        return amount * 0.80  # 20% off


# Adding a new discount doesn't break old code—we just inherit from DiscountStrategy!
class FlashSaleDiscount(DiscountStrategy):
    def apply_discount(self, amount: float) -> float:
        return amount * 0.50  # 50% off


#  Example Usage 

print("# --- SRP & OCP Demonstration ---")

inv = Invoice("Sarah Connor", 200.0)
repo = InvoiceRepository()
repo.save(inv)

# Dynamic strategy selection
discounts = [StandardDiscount(), VIPDiscount(), FlashSaleDiscount()]

for d in discounts:
    discounted_price = d.apply_discount(inv.amount)
    print(f"Final Price using {d.__class__.__name__}: ${discounted_price:.2f}")