class TypeCheck:
    def __new__(cls, name, bases, dct):
        for n, t in dct.get('__annotations__',{}).items():
            if not isinstance(dct[n],t):
                raise TypeError("Attributes types doesnt match with annotations")

class StrictType(metaclass=TypeCheck):
    
    a: int = 5
    b: str = 'asd'
    c: float = 12.3



class StrictType2(metaclass=TypeCheck):
    
    a: int = 5
    b: str = 'asd'
    c: float = 124
