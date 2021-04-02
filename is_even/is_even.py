import requests


def is_even(number):
    n = int(number)
    r = requests.get(f"https://api.isevenapi.xyz/api/iseven/{n}/")
    return r.json()["iseven"]


if __name__ == '__main__':
    if is_even(10):
        print("even")

    if not is_even(3):
        print("odd")
