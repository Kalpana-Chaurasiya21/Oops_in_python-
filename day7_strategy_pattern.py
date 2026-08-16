# Strategy Pattern
# Allows you to define a family of algorithms, put each in a separate class,
# and make their objects interchangeable at runtime.
# Great for replacing messy nested if/else or elif blocks!

from abc import ABC, abstractmethod


# --- Strategy Interface ---
class ShippingStrategy(ABC):
    @abstractmethod
    def calculate_cost(self, weight_kg: float) -> float:
        pass


# --- Concrete Strategies ---
class StandardShipping(ShippingStrategy):
    def calculate_cost(self, weight_kg: float) -> float:
        return weight_kg * 2.50 + 5.00  # Base fee + rate


class ExpressShipping(ShippingStrategy):
    def calculate_cost(self, weight_kg: float) -> float:
        return weight_kg * 5.00 + 15.00


class SameDayShipping(ShippingStrategy):
    def calculate_cost(self, weight_kg: float) -> float:
        return weight_kg * 10.00 + 30.00


# --- Context Class ---
class Order:
    def __init__(self, weight_kg: float, shipping_strategy: ShippingStrategy):
        self.weight_kg = weight_kg
        # Inject the strategy dynamically
        self.shipping_strategy = shipping_strategy

    def set_shipping_strategy(self, shipping_strategy: ShippingStrategy):
        """Allows changing the strategy dynamically at runtime."""
        self.shipping_strategy = shipping_strategy

    def calculate_total_shipping(self) -> float:
        return self.shipping_strategy.calculate_cost(self.weight_kg)


# --- Example Usage ---

print("# --- Strategy Pattern Demonstration ---")

# Order weighing 4.5 kg starting with Standard shipping
my_order = Order(weight_kg=4.5, shipping_strategy=StandardShipping())
print(f"Standard Shipping Cost: ${my_order.calculate_total_shipping():.2f}")

# Customer changes mind to Express at checkout
my_order.set_shipping_strategy(ExpressShipping())
print(f"Express Shipping Cost:  ${my_order.calculate_total_shipping():.2f}")

# Need it immediately
my_order.set_shipping_strategy(SameDayShipping())
print(f"Same-Day Shipping Cost: ${my_order.calculate_total_shipping():.2f}")