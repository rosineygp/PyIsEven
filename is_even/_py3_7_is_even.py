from __future__ import annotations

import requests
from functools import lru_cache
from retry import retry
from typing import TYPE_CHECKING, Union
from ._typings import Success, Error

if TYPE_CHECKING:
    from typing_extensions import TypeGuard

@lru_cache(maxsize=None)
@retry(ConnectionError, tries=3, delay=2)
def is_even(number: Union[str, int]) -> TypeGuard[int]:
    n: int = int(number)
    r: requests.Response = requests.get(f"https://api.isevenapi.xyz/api/iseven/{n}/")

    json: Union[Success, Error] = r.json()

    if r.status_code == requests.codes.ok:
        return json["iseven"]
    else:
        raise Exception(json["error"])


def is_odd(number: Union[str, int]) -> TypeGuard[int]:
    return not is_even(number)
