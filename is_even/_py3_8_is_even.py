from __future__ import annotations

import requests
from functools import lru_cache
from retry import retry
from typing import Iterator, TYPE_CHECKING, Union
from requests.exceptions import RequestException

from ._typings import Success, Error
from ._py3_api_response import IsEven
from ._py_api_exception import IsEvenException

if TYPE_CHECKING:
    from typing_extensions import TypeGuard


@lru_cache(maxsize=None)
@retry(ConnectionError, tries=3, delay=2)
def is_even(number: Union[str, int]) -> TypeGuard[IsEven]:
    n: int = _positive(number)

    if n < 0:
        raise ValueError("number should be a positive")

    try:
        r: requests.Response = requests.get(
            f"https://api.isevenapi.xyz/api/iseven/{n}/"
        )

        json: Union[Success, Error] = r.json()

        if "error" in json:
            raise IsEvenException(json["error"])
        else:
            return IsEven(json["iseven"], json["ad"])
    except RequestException:
        return IsEven(list(_is_even(n))[-1], "Python Software Foundation rocks!")


def is_odd(number: Union[str, int]) -> TypeGuard[int]:
    return not is_even(number)


def _is_even(n: int) -> Iterator[bool]:
    e: bool = False
    for _ in range(n):
        yield e
        e = not e


def _positive(number: Union[str, int]) -> TypeGuard[int]:
    n: int = int(number)

    if n < 0:
        raise ValueError("number should be a positive", n)

    return n
