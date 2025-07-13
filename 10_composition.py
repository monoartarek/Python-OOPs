class Engine:
    def __init__(self, horsepower):
        self.horsepower = horsepower

class Car:
    def __init__(self, brand, power):
        self.brand = brand 
        self.engine = Engine(power) #composition : Car creates Engine inside

    def show_details(self):
        print(f"{self.brand} car has an engine with {self.engine.horsepower} HP")

# Create Car object (engine is created inside it)
car1 = Car("Toyota", 150)

car1.show_details()

