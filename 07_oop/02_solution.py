#Class method and self
# Add a  method to the car class that displays the full name of the car (brand and model)
class Car:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model

    def full_name(self):
        return f"{self.brand} {self.model} "
#inheritance
class ElectricCar(Car):
    def __init__(self,brand,model,battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

my_tesla = ElectricCar("Tesla","Model S","85KWh")
print(my_tesla.model)
print(my_tesla.full_name())

my_car = Car("Toyota","Corolla")
print(my_car.brand)
print(my_car.full_name())

#4.Encapsulation
#Problem:modify the car class to encapsulate the brand attribute, making it private, and provide a getter method for it
