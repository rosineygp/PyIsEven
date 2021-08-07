import requests
from functools import lru_cache
from retry import retry
from typing_extensions import TypeGuard
from requests.exceptions import RequestException, ConnectTimeout

from ._typings import Success, Error
from ._py3_api_response import IsEven


@lru_cache(maxsize=None)
@retry(ConnectionError, tries=3, delay=2)
def is_even(number: str | int) -> TypeGuard[int]:
    n: int = int(number)

    try:
        r: requests.Response = requests.get(
            f"https://api.isevenapi.xyz/api/iseven/{n}/"
        )

        json: Success | Error = r.json()

        if "error" in json:
            raise Exception(json["error"])
        else:
            return IsEven(json["iseven"], json["ad"])
    except (RequestException, ConnectTimeout):
        return IsEven(_is_even(n), "Python Software Foundation rocks!")


def is_odd(number: str | int) -> TypeGuard[int]:
    return not is_even(number)


def _is_even(n: int):
    e: bool = False
    for _ in range(n):
        yield e
        e = not e
