# Decorator Pattern
# Dynamically attaches new behaviors to an object at runtime by wrapping it.
# Unlike standard inheritance (which applies static behavior to an entire class),
# decorators wrap individual instances so you can layer behaviors flexibly.

from abc import ABC, abstractmethod


#  Component Interface 
class Coffee(ABC):
    @abstractmethod
    def get_cost(self) -> float:
        pass

    @abstractmethod
    def get_description(self) -> str:
        pass


#  Concrete Component 
class BasicCoffee(Coffee):
    def get_cost(self) -> float:
        return 3.00

    def get_description(self) -> str:
        return "Basic Coffee"


#  Base Decorator 
class CoffeeDecorator(Coffee):
    def __init__(self, coffee: Coffee):
        self._decorated_coffee = coffee

    def get_cost(self) -> float:
        return self._decorated_coffee.get_cost()

    def get_description(self) -> str:
        return self._decorated_coffee.get_description()


# Concrete Decorators 

class MilkDecorator(CoffeeDecorator):
    def get_cost(self) -> float:
        return super().get_cost() + 0.50

    def get_description(self) -> str:
        return super().get_description() + ", Steamed Milk"


class VanillaDecorator(CoffeeDecorator):
    def get_cost(self) -> float:
        return super().get_cost() + 0.75

    def get_description(self) -> str:
        return super().get_description() + ", Vanilla Syrup"


class WhippedCreamDecorator(CoffeeDecorator):
    def get_cost(self) -> float:
        return super().get_cost() + 1.00

    def get_description(self) -> str:
        return super().get_description() + ", Whipped Cream"


#  Example Usage 

print("# --- Decorator Pattern Demonstration ---")

# Start with plain coffee
order = BasicCoffee()
print(f"Order: {order.get_description()} | Cost: ${order.get_cost():.2f}")

# Dynamically wrap it with additions
order_with_milk = MilkDecorator(order)
order_deluxe = WhippedCreamDecorator(VanillaDecorator(order_with_milk))

print(f"Order: {order_deluxe.get_description()}")
print(f"Total Cost: ${order_deluxe.get_cost():.2f}")