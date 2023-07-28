class Singletone(type):
    instance = None

    def __new__(cls, name, bases, dct):
        return super().__new__(cls, name, bases, dct)

    def __call__(cls):
        if cls.instance is None:
            cls.instance = cls
        return cls.instance


class Hundred(metaclass=Singletone):
    pass


db = Hundred()
db1 = Hundred()

print(db1 is db)
