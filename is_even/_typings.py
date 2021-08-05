from typing import TypedDict


class Success(TypedDict):
    ad: str
    iseven: bool


class Error(TypedDict):
    error: str


class ISEVEN_APIresponse(int):
    def __new__(self, value, ad):
        self.ad = ad
        self.value = value
        return int.__new__(self, bool(value))
