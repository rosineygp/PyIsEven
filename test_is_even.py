import unittest
from sys import version_info

from is_even import is_even


class TestIsEven(unittest.TestCase):
    def test_even(self):
        even = is_even.is_even(2).is_even
        self.assertTrue(even)

    def test_odd(self):
        odd = is_even.is_odd(3)
        self.assertTrue(odd)

    def test_not_even(self):
        even = is_even.is_even(3).is_even
        self.assertFalse(even)

    def test_not_odd(self):
        even = is_even.is_odd(2)
        self.assertFalse(even)

    def test_cache(self):
        self.assertTrue(is_even.is_even(2).is_even)
        self.assertFalse(is_even.is_even(3).is_even)

    def test_negative(self):
        with self.assertRaises(Exception):
            is_even.is_even(-10)

    def test_failback_even(self):
        v = 2
        if version_info >= (3, 0):
            even = list(is_even._is_even(v))[-1]
        else:
            even = is_even._is_even(v)
        self.assertTrue(even)

    def test_failback_odd(self):
        v = 3
        if version_info >= (3, 0):
            odd = list(is_even._is_even(v))[-1]
        else:
            odd = is_even._is_even(v)
        self.assertFalse(odd)


if __name__ == "__main__":
    unittest.main()
