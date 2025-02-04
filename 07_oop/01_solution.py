#Basic class and object
#Problem:create acar class with attributes like brand and model.then create an instace of this class
class Car:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model
        # understanding purpuse assume that above code is like a
        #  empty form below code is like we can create any number of users or cars


my_car = Car("Toyota","Corolla")
print(my_car.brand)
print(my_car.model)

my_new_car = Car("Tata","safari")
print(my_new_car.model)
