import unittest

from is_even import is_even


class TestIsEven(unittest.TestCase):
    def test_even(self):
        even = is_even.is_even(2)
        self.assertTrue(even)

    def test_odd(self):
        odd = is_even.is_odd(3)
        self.assertTrue(odd)

    def test_not_even(self):
        even = is_even.is_even(3)
        self.assertFalse(even)

    def test_not_odd(self):
        even = is_even.is_odd(2)
        self.assertFalse(even)

    def test_cache(self):
        self.assertTrue(is_even.is_even(2))
        self.assertFalse(is_even.is_even(3))

    def test_negative(self):
        with self.assertRaises(Exception):
            is_even.is_even(-10)


if __name__ == "__main__":
    unittest.main()
