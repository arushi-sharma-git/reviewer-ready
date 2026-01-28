import unittest
from utils import is_key_safe

class TestSecuritySystem(unittest.TestCase):

    def test_valid_key(self):
        """Should return True for a perfect 8-char alphanumeric key."""
        is_valid, msg = is_key_safe("A1234567")
        self.assertTrue(is_valid)

    def test_too_short(self):
        """Should return False if key is less than 8 characters."""
        is_valid, msg = is_key_safe("A123")
        self.assertFalse(is_valid)
        self.assertIn("Pattern Mismatch", msg)

    def test_prohibited_symbols(self):
        """Should return False if key contains symbols like @ or #."""
        is_valid, msg = is_key_safe("A123@567")
        self.assertFalse(is_valid)

    def test_lowercase_start(self):
        """Should return False if it starts with a lowercase letter."""
        # Our regex r"^[A-Z]" requires Uppercase!
        is_valid, msg = is_key_safe("a1234567")
        self.assertFalse(is_valid)

if __name__ == "__main__":
    unittest.main()