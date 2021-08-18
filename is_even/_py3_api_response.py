class IsEven:
    def __init__(self, value: int, ad: str) -> bool:
        self.ad = ad
        self.value = value

    def __repr__(self) -> str:
        return str(self.value)

    def __bool__(self):
        return self.value
