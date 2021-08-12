import requests
from functools import lru_cache
from retry import retry
from typing import Union, Iterator
from requests.exceptions import RequestException
from ._py3_api_response import IsEven
from ._py_api_exception import IsEvenException


@lru_cache(maxsize=None)
@retry(ConnectionError, tries=3, delay=2)
def is_even(number: Union[str, int]) -> bool:
    n: int = _positive(number)

    try:
        r = requests.get(f"https://api.isevenapi.xyz/api/iseven/{n}/")

        if "error" in r.json():
            raise IsEvenException(r.json()["error"])
        else:
            return IsEven(r.json()["iseven"], r.json()["ad"])
    except RequestException:
        return IsEven(list(_is_even(n))[-1], "Python Software foundation rocks!")


def is_odd(number: Union[str, int]) -> bool:
    return not is_even(number)


def _is_even(n: int) -> Iterator[bool]:
    e: bool = False
    for _ in range(n):
        yield e
        e = not e


def _positive(number: Union[str, int]) -> int:
    n: int = int(number)

    if n < 0:
        raise ValueError("number should be a positive", n)

    return n
