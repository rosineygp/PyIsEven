import requests


def is_even(number):
    n = int(number)

    if n < 0:
        raise Exception

    try:
        r = requests.get("https://api.isevenapi.xyz/api/iseven/" + str(n) + "/")

        if r.ok:
            return r.json()["iseven"]
        else:
            raise Exception(r.json()["error"])
    except Exception:
        return _is_even(n)


def is_odd(number):
    return not is_even(number)


def _is_even(n):
    e = True
    for _ in range(n):
        e = not e
    return e
