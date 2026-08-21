# Testing OOP Code: Unit Testing & Mocking
# Demonstrates how Dependency Injection makes classes easy to test in isolation
# using Python's native 'unittest' framework and 'unittest.mock.MagicMock'.

import unittest
from unittest.mock import MagicMock
from abc import ABC, abstractmethod


#  Service Interface & Real Implementation 

class PaymentGateway(ABC):
    @abstractmethod
    def process_charge(self, amount: float, card_token: str) -> bool:
        pass


class StripeGateway(PaymentGateway):
    """Real implementation that would talk to an external API."""
    def process_charge(self, amount: float, card_token: str) -> bool:
        print("[Stripe API] Making real HTTP network request...")
        # Imagine real API call here
        return True


#  Domain Class to Test 

class OrderProcessor:
    """High-level class relying on injected PaymentGateway."""
    def __init__(self, gateway: PaymentGateway):
        self.gateway = gateway

    def checkout(self, order_id: str, amount: float, card_token: str) -> str:
        if amount <= 0:
            raise ValueError("Order amount must be greater than zero.")
        
        # Calls injected payment service
        success = self.gateway.process_charge(amount, card_token)
        
        if success:
            return f"ORDER-{order_id}-SUCCESS"
        return f"ORDER-{order_id}-FAILED"


# Unit Test Suite 

class TestOrderProcessor(unittest.TestCase):
    """Isolated test suite using mock objects."""

    def setUp(self):
        # Create a mock object implementing the PaymentGateway interface
        self.mock_gateway = MagicMock(spec=PaymentGateway)
        # Inject the fake dependency into OrderProcessor
        self.processor = OrderProcessor(self.mock_gateway)

    def test_successful_checkout(self):
        # Configure mock behavior
        self.mock_gateway.process_charge.return_value = True

        result = self.processor.checkout("1001", 150.00, "tok_visa_123")

        # Assertions
        self.assertEqual(result, "ORDER-1001-SUCCESS")
        # Verify the mock was called with exact expected arguments
        self.mock_gateway.process_charge.assert_called_once_with(150.00, "tok_visa_123")

    def test_failed_checkout_from_gateway(self):
        # Simulate gateway declining card
        self.mock_gateway.process_charge.return_value = False

        result = self.processor.checkout("1002", 50.00, "tok_declined")

        self.assertEqual(result, "ORDER-1002-FAILED")

    def test_invalid_amount_raises_exception(self):
        # Verify edge cases fail early without reaching the payment gateway
        with self.assertRaises(ValueError):
            self.processor.checkout("1003", -10.00, "tok_visa_123")
        
        # Verify gateway was never called
        self.mock_gateway.process_charge.assert_not_called()


if __name__ == "__main__":
    print("# --- Running OOP Unit Tests with Mock Dependencies ---")
    unittest.main(verbosity=2)