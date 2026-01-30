class Shape:
    def area(self):
        raise NotImplementedError("Subclasses must implement area")
class Circle(Shape):
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        return 3.14*self.radius**2
class Rectangle(Shape):
    def __init__(self,l,b):
        self.length=l
        self.breadth=b
    def area(self):
        return self.length*self.breadth
class Triangle(Shape):
    def __init__(self,base,height):
        self.base=base
        self.height=height
    def area(self):
        return 0.5*self.base*self.height
c1=Circle(3)
r1=Rectangle(3,4)
t1=Triangle(3,4)
print(c1.area())
print(r1.area())
print(t1.area())