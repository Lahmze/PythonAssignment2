class Vehicle:
    """Base class representing a generic vehicle."""

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def describe(self):
        print(f"{self.brand} {self.model} is a vehicle.")

    def start_engine(self):
        print("The vehicle starts.")


class Car(Vehicle):
    """Car subclass overriding start_engine()."""

    def __init__(self, brand, model, num_doors):
        super().__init__(brand, model)
        self.num_doors = num_doors

    def start_engine(self):
        print(f"{self.brand} {self.model}: Turn the key, and the engine roars to life.")

    def describe(self):
        super().describe()
        print(f"It has {self.num_doors} doors.")


class Bike(Vehicle):
    """Bike subclass overriding start_engine()."""

    def __init__(self, brand, model, has_gears):
        super().__init__(brand, model)
        self.has_gears = has_gears

    def start_engine(self):
        print(f"{self.brand} {self.model}: No engine — just start pedaling!")

    def describe(self):
        super().describe()
        gear_info = "has gears" if self.has_gears else "is a single-speed"
        print(f"It {gear_info}.")


def main():
    vehicles = [
        Car("Toyota", "Corolla", 4),
        Bike("BMX", "6", True),
        Vehicle("Chinese", "Model"),
    ]

    for v in vehicles:
        v.describe()
        v.start_engine()
        print()


if __name__ == '__main__':
    main()