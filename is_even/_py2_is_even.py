import requests
from requests.exceptions import RequestException, ConnectTimeout


class ISEVEN_APIresponse(object):
    def __init__(self, is_even, ad):
        self.is_even = is_even
        self.ad = ad


def is_even(number):
    n = int(number)

    if n < 0:
        raise Exception

    try:
        r = requests.get("https://api.isevenapi.xyz/api/iseven/" + str(n) + "/")

        if "error" in r.json():
            raise Exception(r.json()["error"])
        else:
            return ISEVEN_APIresponse(r.json()["iseven"], r.json()["ad"])
    except (RequestException, ConnectTimeout):
        return ISEVEN_APIresponse(_is_even(n), "Python Software Foundation rocks!")


def is_odd(number):
    return not is_even(number).is_even


def _is_even(n):
    e = True
    for _ in range(n):
        e = not e
    return e
