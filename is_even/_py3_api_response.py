class IsEven(int):
    def __new__(cls, value: int, ad: str) -> int:
        cls.ad = ad
        cls.value = value
        return int.__new__(cls, bool(value))

    def __repr__(self) -> str:
        return str(bool(self.value))
