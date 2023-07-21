import weakref


class ValidType:
    def __init__(self, type) -> None:
        self.data = weakref.WeakKeyDictionary()
        self.type = type

    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, instance, owner=None):
        if instance is None:
            return self
        return self.data.get(instance, None)

    def __set__(self, instance, value):
        if isinstance(value, self.type):
            self.data[instance] = value
        raise TypeError(f'Incorrect type. Use {self.type}')


class DescInt(ValidType):
    def __init__(self) -> None:
        super().__init__(int)


class DescStr(ValidType):
    def __init__(self) -> None:
        super().__init__(str)


class DescFloat(ValidType):
    def __init__(self) -> None:
        super().__init__(float)


class DescList(ValidType):
    def __init__(self) -> None:
        super().__init__(list)


