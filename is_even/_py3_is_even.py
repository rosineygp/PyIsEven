import requests
from functools import lru_cache
from retry import retry
from typing import Union


@lru_cache(maxsize=None)
@retry(ConnectionError, tries=3, delay=2)
def is_even(number: Union[str, int]) -> bool:
    n = int(number)

    try:
        r = requests.get(f"https://api.isevenapi.xyz/api/iseven/{n}/")

        if r.status_code == requests.codes.ok:
            return r.json()["iseven"]
        else:
            raise Exception(r.json()["error"])
    except Exception:
        return list(_is_even(n))[-1]


def is_odd(number: Union[str, int]) -> bool:
    return not is_even(number)


def _is_even(n: int):
    e: bool = False
    for _ in range(n):
        yield e
        e = not e
