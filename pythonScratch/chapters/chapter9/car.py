class Car:
    def __init__(self, make, model, year) -> None:
        self.make = make
        self.model = model
        self.year = year
        self.read_odometer = 40

    def get_descriptive_name(self):
        return f"{self.make} {self.model} {self.year}"

    def read_odometer(self):
        print(f"This car has {self.read_odometer} miles on it.")

    def update_odometer(self, mileage):
        if mileage >= self.read_odometer:
            self.read_odometer = mileage
        else:
            print(f"You can not rollback the odometer!")

    def increment_odometer(self, miles):
        self.read_odometer += miles
