class MyClass:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def print_values(self):
        print("x:", self.x)
        print("y:", self.y)

# Creating an object of MyClass
obj = MyClass(10, 20)

# Calling the print_values method using the object
obj.print_values()




class Subject:

	def __init__(self, attr1, attr2):
		self.attr1 = attr1
		self.attr2 = attr2


obj = Subject('Maths', 'Science')
print(obj.attr1) 
print(obj.attr2)
