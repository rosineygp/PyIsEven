#!/usr/bin/env python

import requests
from functools import lru_cache
from retry import retry
from typing import Union


@lru_cache(maxsize=None)
@retry(ConnectionError, tries=3, delay=2)
def is_even(number):
    n = int(number)
    r = requests.get(f"https://api.isevenapi.xyz/api/iseven/{n}/")

    if r.status_code == requests.codes.ok:
        return r.json()["iseven"]
    else:
        raise Exception(r.json()["error"])


def is_odd(number):
    return not is_even(number)
