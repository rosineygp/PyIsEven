import requests
from functools import lru_cache
from retry import retry
from typing_extensions import TypeGuard
from ._typings import Success, Error

@lru_cache(maxsize=None)
@retry(ConnectionError, tries=3, delay=2)
def is_even(number: str | int) -> TypeGuard[int]:
    n: int = int(number)
    r: requests.Response = requests.get(f"https://api.isevenapi.xyz/api/iseven/{n}/")

    json: Success | Error = r.json()

    if r.status_code == requests.codes.ok:
        return json["iseven"]
    else:
        raise Exception(json["error"])


def is_odd(number: str | int) -> TypeGuard[int]:
    return not is_even(number)
