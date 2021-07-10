from typing_extensions import TypeGuard
import requests
from functools import lru_cache
from retry import retry
from typing import Union, TypeGuard
from ._typings import Success, Error

@lru_cache(maxsize=None)
@retry(ConnectionError, tries=3, delay=2)
def is_even(number: str | int) -> TypeGuard[int]:
    n: int = int(number)
    r: requests.Response = requests.get(f"https://api.isevenapi.xyz/api/iseven/{n}/")

    json: Success | Error = r.json()

    if r.status_code == requests.codes.ok:
        assert isinstance(json, Success)
        return json["iseven"]
    else:
        assert isinstance(json, Error)
        raise Exception(json["error"])


def is_odd(number: str | int) -> TypeGuard[int]:
    return not is_even(number)
