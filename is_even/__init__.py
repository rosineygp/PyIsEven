# from .is_even import is_even


class ISEVEN_APIresponse(int):
    def __new__(self, value, ad):
        self.ad = ad
        self.value = value
        return int.__new__(self, bool(value))
