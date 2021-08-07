import requests
from functools import lru_cache
from retry import retry
from typing import Union
from requests.exceptions import RequestException, ConnectTimeout
from ._py3_api_response import IsEven


@lru_cache(maxsize=None)
@retry(ConnectionError, tries=3, delay=2)
def is_even(number: Union[str, int]) -> bool:
    n = int(number)

    try:
        r = requests.get(f"https://api.isevenapi.xyz/api/iseven/{n}/")

        if "error" in r.json():
            raise Exception(r.json()["error"])
        else:
            return IsEven(r.json()["iseven"], r.json()["ad"])
    except (RequestException, ConnectTimeout):
        return IsEven(_is_even(n), "Python Software foundation rocks!")


def is_odd(number: Union[str, int]) -> bool:
    return not is_even(number)


def _is_even(n: int):
    e: bool = False
    for _ in range(n):
        yield e
        e = not e
