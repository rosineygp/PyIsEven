import requests
from requests.exceptions import RequestException
from ._py_api_exception import IsEvenException


class IsEven:
    def __init__(self, value, ad):
        self.ad = ad
        self.value = value

    def __repr__(self):
        return str(self.value)

    def __nonzero__(self):
        return self.value


def is_even(number):
    n = _positive(number)

    try:
        r = requests.get("https://api.isevenapi.xyz/api/iseven/" + str(n) + "/")

        if "error" in r.json():
            raise IsEvenException(r.json()["error"])
        else:
            return IsEven(r.json()["iseven"], r.json()["ad"])
    except RequestException:
        return IsEven(_is_even(n), "Python Software Foundation rocks!")


def is_odd(number):
    return not is_even(number)


def _is_even(n):
    e = True
    for _ in range(n):
        e = not e
    return e


def _positive(number):
    n = int(number)

    if n < 0:
        raise ValueError("number should be a positive", n)

    return n
