import unittest

from is_even import is_even


class TestIsEven(unittest.TestCase):
    def test_even(seff):
        even = is_even.is_even(2)
        assert (even is True)

    def test_odd(self):
        odd = is_even.is_odd(3)
        assert(odd is True)

    def test_not_even(self):
        even = is_even.is_even(3)
        assert (even is False)

    def test_not_odd(self):
        even = is_even.is_odd(2)
        assert (even is False)

    def test_cache(self):
        assert (is_even.is_even(2) is True)
        assert (is_even.is_even(3) is False)

    def test_negative(self):
        try:
            is_even.is_even(-10)
        except Exception:
            pass


if __name__ == "__main__":
    unittest.main()
