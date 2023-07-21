from descriptors import DescFloat,DescInt,DescList,DescStr

class Person:
    age = DescInt()
    height = DescFloat()
    name = DescStr()
    tags = DescList()
    favorite_food = DescList()

    def __init__(self, age, height, tags, favorite_foods, name) -> None:
        self.age = age
        self.height = height
        self.tags = tags
        self.favorite_food = favorite_foods
        self.name = name

