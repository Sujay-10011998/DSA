class Animal:
    def display1(self):
        print("1")

class Dog(Animal):
    def display2(self):
        print("2")

class Cat(Animal):
    def speak(self):
        return "2"


d = Dog()
d.display1()
d.display2()
c = Cat()
c.display1()
