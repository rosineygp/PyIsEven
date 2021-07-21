from sys import version_info

__all__ = (
    'is_even',
    'is_odd',
)

if version_info >= (3, 10):
    from ._py3_10_is_even import is_even, is_odd
elif version_info >= (3, 7):
    from ._py3_7_is_even import is_even, is_odd
elif version_info >= (3, 0):
    from ._py3_is_even import is_even, is_odd
else:
    from ._py3_is_even import is_even, is_odd
