from .is_even import is_even

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
