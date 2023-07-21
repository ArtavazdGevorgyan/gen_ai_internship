
class Int:
    def __init__(self, min_value=None, max_value=None) -> None:
        self.min = min_value
        self.max = max_value

    def __set_name__(self, owner, name):
        self.name = name

    def __set__(self, instance, value):
        if not isinstance(value, int):
            raise ValueError(f"Value must be an integer")

        if (self.min is not None and value < self.min) or (self.max is not None and value > self.max):
            raise ValueError(
                f"Value must be in ({self.min}, {self.max}) range")

        instance.__dict__[self.name] = value

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance.__dict__[self.name]
