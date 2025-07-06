from car import Car


class ElectricCar(Car):
    def __init__(self, make, model, year) -> None:
        super().__init__(make, model, year)
        self.battery = Battery()


class Battery:
    def __init__(self, battery=40) -> None:
        self.battery = battery

    def describe_battery(self):
        print(f"This car has {self.battery} KWh on it.")

    def get_range(self):
        if self.battery == 40:
            range = 150
        elif self.battery == 65:
            range = 225
        print(f"This car go about {range} miles on a full charge.")
