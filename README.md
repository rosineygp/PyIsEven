# Is Even

![PyPI - Downloads](https://img.shields.io/pypi/dm/PyIsEven)
[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=rosineygp_PyIsEven&metric=alert_status)](https://sonarcloud.io/dashboard?id=rosineygp_PyIsEven)

Check if interger is even using `isevenapi`.

https://isevenapi.xyz/

Main features:

- cache memoization
- api retry handler
- hide ads

## Install

```bash
pip install PyIsEven
```

## Usage

```python
from is_even import is_even as ie

ie.is_even(10)
> True

# Get AD
v = ie.is_even(10)

v.ad
> "HONDA CIVIC '96, AM/FM/CD, low miles, Good condition. Speaks Spanish $3500 339-555-6289"

ie.is_even(10).ad
> "CHINA CABINET, buffet, hutch solid pine, 6.5 tall x 4.5 wide, lighted windows. few cat scratches but cat has died. $700. Call 435-555-6421"
```