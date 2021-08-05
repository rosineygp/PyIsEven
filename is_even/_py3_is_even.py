import requests
from functools import lru_cache
from retry import retry
from typing import Union
from ._typings import ISEVEN_APIresponse
from requests.exceptions import RequestException, ConnectTimeout


@lru_cache(maxsize=None)
@retry(ConnectionError, tries=3, delay=2)
def is_even(number: Union[str, int]) -> bool:
    n = int(number)

    try:
        r = requests.get(f"https://api.isevenapi.xyz/api/iseven/{n}/")

        if "error" in r.json():
            raise Exception(r.json()["error"])
        else:
            return ISEVEN_APIresponse(r.json()["iseven"], r.json()["ad"])
    except (RequestException, ConnectTimeout):
        return ISEVEN_APIresponse(_is_even(n), "Python Software foundation rocks!")


def is_odd(number: Union[str, int]) -> bool:
    return not is_even(number)


def _is_even(n: int):
    e: bool = False
    for _ in range(n):
        yield e
        e = not e
