from sys import version_info

__all__ = ("is_even", "is_odd", "_is_even")

if version_info >= (3, 10):
    from ._py3_10_is_even import is_even, is_odd, _is_even
elif version_info >= (3, 8):
    from ._py3_8_is_even import is_even, is_odd, _is_even
elif version_info >= (3, 0):
    from ._py3_is_even import is_even, is_odd, _is_even
else:
    from ._py2_is_even import is_even, is_odd, _is_even
