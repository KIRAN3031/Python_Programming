from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Rectangle(Shape):
    def __init__(self,width,height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2*(self.width + self.height)


class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius
    
    def area(self):
        return 3.14 * self.radius * self.radius
    
    def perimeter(self):
        return 2 * 3.14 * self.radius
    
r1 = Rectangle(10,20)
print()
print(f"Area of rectangle is {r1.area()}")
print(f"Perimeter of rectangle is {r1.perimeter()}")
c1 = Circle(7)
print()
print(f"Area of circle is {c1.area()}")
print(f"Perimeter of circle is {c1.perimeter()}")