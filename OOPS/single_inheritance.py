class Animal:
    def __init__(self,name,colour):
        self.name = name
        self.colour = colour
    
    def display(self):
        print(self.name)
        print(self.colour)
        
class Tiger(Animal):
    def __init__(self,name,colour,number,food):
        self.number = number
        self.food = food
        Animal.__init__(self,name,colour)
        
    def output(self):
        print(self.name)
        print(self.colour)
        print(self.number)
        print(self.food)
        
t = Tiger("Jack", "yellow-black", 1, "meat")
t.display()
t.output()
