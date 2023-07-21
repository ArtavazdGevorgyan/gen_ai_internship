from type import Int


class Point2D:
    x = Int(min_value=0)
    y = Int(min_value=0)

    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y


class Point2DSequence:
    def __init__(self, min_len=None, max_len=None) -> None:
        self.min_len = min_len
        self.max_len = max_len

    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, instance, owner):
        if instance is None:
            return self

        return instance.__dict__.get(self.name, None)

    def __set__(self, instance, value):
        print("Length:", len(value))
        if (self.min_len is not None and self.min_len > len(value)) or (self.max_len is not None and self.max_len < len(value)):
            raise ValueError(
                f"Length must be in ({self.min_len}, {self.max_len}) range")

        if isinstance(value, (list, tuple)):
            for item in value:
                if not isinstance(item, Point2D):
                    raise ValueError("Each element must be Point2D type...")
        else:
            raise ValueError(f"Value must be type list or tuple...")

        instance.__dict__[self.name] = value
