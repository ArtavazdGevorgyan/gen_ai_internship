class Vehicle:
    def __init__(self, year, model):
        self.year = year
        self.model = model

    def description(self):
        return f"{self.year} {self.model}"


class Car(Vehicle):
    def __init__(self, model, year, color):
        super().__init__(model, year)
        self.color = color

    def description(self):
        return f"{super().description()} {self.color}"


class Motorcycle(Vehicle):
    def __init__(self, model, year, num_wheels):
        super().__init__(model, year)
        self.num_wheels = num_wheels

    def description(self):
        return f"{super().description()}, {self.num_wheels} wheels"


class Bicycle(Vehicle):
    def __init__(self, model, year, build_country):
        super().__init__(model, year)
        self.build_country = build_country

    def description(self):
        return f"{super().description()}, build in {self.build_country}"
