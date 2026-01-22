class Vehicle:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
    def displayDetails(self):
        print(self.brand)
        print(self.model)
class Car(Vehicle):
    def __init__(self,brand,model,seats):
        super().__init__(brand,model)
        self.seats=seats
    def displayDetails(self):
        print("Car")
        super().displayDetails()
        print(self.seats)
class Bike(Vehicle):
    def __init__(self,brand,model,cc):
        super().__init__(brand,model)
        self.cc=cc
    def displayDetails(self):
        print("Bike")
        super().displayDetails()
        print(self.cc)

c=Car("BMW","520d",4)
b=Bike("Yamaha","R15",155)
c.displayDetails()
b.displayDetails()