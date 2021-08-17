class IsEven(int):
    def __new__(cls, value: int, ad: str) -> bool:
        cls.ad = ad
        cls.value = value
        return bool(value)

    def __repr__(self) -> str:
        return str(bool(self.value))
