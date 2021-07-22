from typing import TypedDict


class Success(TypedDict):
    ad: str
    iseven: bool


class Error(TypedDict):
    error: str
