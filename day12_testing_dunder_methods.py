# Testing OOP Code: Testing Dunder Operators & Encapsulation
# Shows how to write comprehensive unit tests for custom object equality,
# mathematical dunder methods, and private encapsulation boundaries.

import unittest


class BankAccount:
    """Domain class with encapsulated balance and custom comparison operators."""

    def __init__(self, account_number: str, initial_balance: float = 0.0):
        self.account_number = account_number
        self._balance = initial_balance  # Encapsulated state

    @property
    def balance(self) -> float:
        return self._balance

    def deposit(self, amount: float):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self._balance += amount

    def __eq__(self, other) -> bool:
        """Equality comparison by account number."""
        if isinstance(other, BankAccount):
            return self.account_number == other.account_number
        return False

    def __add__(self, other):
        """Combines balances of two accounts into a new temporary instance."""
        if isinstance(other, BankAccount):
            return BankAccount("MERGED-TEMP", self._balance + other._balance)
        raise TypeError("Can only merge BankAccount with another BankAccount.")


#  Test Suite 

class TestBankAccount(unittest.TestCase):

    def test_initial_balance_and_deposit(self):
        acc = BankAccount("ACC-01", 100.0)
        self.assertEqual(acc.balance, 100.0)
        
        acc.deposit(50.0)
        self.assertEqual(acc.balance, 150.0)

    def test_invalid_deposit_throws_error(self):
        acc = BankAccount("ACC-02", 50.0)
        with self.assertRaises(ValueError):
            acc.deposit(-20.0)

    def test_account_equality(self):
        acc1 = BankAccount("ACC-100", 500.0)
        acc2 = BankAccount("ACC-100", 1200.0)  # Same ID, different balance
        acc3 = BankAccount("ACC-200", 500.0)

        self.assertEqual(acc1, acc2)  # Should evaluate as equal via __eq__
        self.assertNotEqual(acc1, acc3)

    def test_account_addition(self):
        acc1 = BankAccount("ACC-1", 300.0)
        acc2 = BankAccount("ACC-2", 200.0)

        merged = acc1 + acc2  # Triggers __add__
        self.assertIsInstance(merged, BankAccount)
        self.assertEqual(merged.balance, 500.0)


if __name__ == "__main__":
    print("\n# --- Running Dunder & State Unit Tests ---")
    unittest.main(verbosity=2)