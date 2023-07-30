class SlottedStruct(type):
    def __new__(cls, name, bases, dct):
        dim = dct.get("dim",False)
        
        if not dim:
            raise ValueError("Add dim of the point")
        
        dct["dim"] = dim
        dct["__slots__"] = ["_coords"]

        def __init__(self, *args):
            if len(args) != dim:
                raise ValueError("Not enough arguments")
            self._coords = tuple(args)
            
        dct["__init__"] = __init__

        def __str__(self):
            return f"{self.__class__.__name__}{self._coords}"
        dct["__str__"] = __str__

        def __eq__(self, other):
            if not isinstance(other, self.__class__):
                return False
            return self._coords == other._coords
        dct["__eq__"] = __eq__

        def __hash__(self):
            return hash(self._coords)
        dct["__hash__"] = __hash__

        return super().__new__(cls, name, bases, dct)
