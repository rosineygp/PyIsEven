import requests
from requests.exceptions import RequestException, ConnectTimeout
from ._typings import ISEVEN_APIresponse


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
    return not is_even(number)


def _is_even(n):
    e = True
    for _ in range(n):
        e = not e
    return e
