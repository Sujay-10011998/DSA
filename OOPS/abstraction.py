from abc import ABC, abstractmethod

#This line imports the ABC (Abstract Base Class) module and the abstractmethod decorator from the abc module.
# ABC is used as a base class for creating abstract classes, and abstractmethod is a decorator
# which is used to declare abstract methods within those classes.




class Shape(ABC):
    # Abstract method that must be implemented by subclasses
    @abstractmethod
    def area(self):
        pass

    # Abstract method that must be implemented by subclasses
    @abstractmethod
    def perimeter(self):
        pass

# Subclass Circle that inherits from Shape
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    # Implementing the abstract method area for Circle
    def area(self):
        return 3.14 * self.radius * self.radius

    # Implementing the abstract method perimeter for Circle
    def perimeter(self):
        return 2 * 3.14 * self.radius



# Create objects of the subclasses and calculate their area and perimeter
circle = Circle(5)
print("Circle Area:", circle.area())
print("Circle Perimeter:", circle.perimeter())