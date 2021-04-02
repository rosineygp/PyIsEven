import unittest

from is_even import is_even


class TestIsEven(unittest.TestCase):
    def test_even(seff):
        even = is_even.is_even(2)
        assert (even is True)

    def test_odd(self):
        odd = is_even.is_even(3)

        assert(odd is False)

    def test_cache(self):
        assert (is_even.is_even(2) is True)
        assert (is_even.is_even(3) is False)

    def test_negative(self):
        try:
            negative = is_even.is_even(-10)
        except Exception as err:
            pass


if __name__ == "__main__":
    unittest.main()
