class Vehicle:
    brand=None
    model=None
class Car(Vehicle):
    def __init__(self,brand,model,seats):
        self.brand=brand
        self.model=model
        self.seats=seats
    def displayDetails(self):
        print("Car")
        print(self.brand)
        print(self.model)
        print(self.seats)
class Bike(Vehicle):
    def __init__(self,brand,model,cc):
        self.brand=brand
        self.model=model
        self.cc=cc
    def displayDetails(self):
        print("Bike")
        print(self.brand)
        print(self.model)
        print(self.cc)

c=Car("BMW","520d",4)
b=Bike("Yamaha","R15",155)
c.displayDetails()
b.displayDetails()