# Multiple Inheritance

class Father:
    def skills(self):
        print("Father: Gardening, Cooking")

class Mother:
    def skills(self):
        print("Mother: Painting, Dancing")

class Child(Father, Mother):
    def skills(self):
        print("Child inherits:")
        Father.skills(self)
        Mother.skills(self)

# Usage
child = Child()
child.skills()
