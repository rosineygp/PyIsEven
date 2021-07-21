import requests


def is_even(number):
    n = int(number)
    r = requests.get("https://api.isevenapi.xyz/api/iseven/" + str(n) + "/")

    if r.ok:
        return r.json()["iseven"]
    else:
        raise Exception(r.json()["error"])


def is_odd(number):
    return not is_even(number)
