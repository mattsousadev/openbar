class EqualAttributes:
    def __eq__(self, __value: object) -> bool:
        if not isinstance(__value, self.__class__):
            return False
        for attr in self.__dict__:
            if not hasattr(__value, attr) or getattr(self, attr) != getattr(__value, attr):
                return False
        return True