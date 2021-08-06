class ISEVEN_APIresponse(int):
    def __new__(self, value: int, ad: str) -> int:
        self.ad = ad
        self.value = value
        return int.__new__(self, bool(value))

    def __repr__(self) -> str:
        return str(bool(self.value))
