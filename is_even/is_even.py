import requests
import functools
from retry import retry


@functools.lru_cache(maxsize=None)
@retry(ConnectionError, tries=3, delay=2)
def is_even(number):
    n = int(number)
    r = requests.get(f"https://api.isevenapi.xyz/api/iseven/{n}/")
    return r.json()["iseven"]


if __name__ == '__main__':

    for i in range(10):
        if is_even(i):
            print(f"{i} is even")
        else:
            print(f"{i} is odd")

    print("second run with cache memo")

    for i in range(10):
        if is_even(i):
            print(f"{i} even")
        else:
            print(f"{i} is odd")
