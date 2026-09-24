class Student:
    def __init__(self,name,age):
        self.name = name
        self.age = age

info = Student("sujay",25)
print(info.name, info.age)





class Student:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def output(self):
        print("name is: " +info.name+ "age is: "+info.age)  
info = Student("sujay",25)
print(info.name, info.age)






class Dog:
	def __init__(self, name):
		self.name = name
		
	def speak(self):
		print("My name is {}".format(self.name))

Rodger = Dog("Rodger")
Tommy = Dog("Tommy")

Rodger.speak()
Tommy.speak()







class Dog:
	attr1 = "mammal"
	def __init__(self, name):
		self.name = name

Rodger = Dog("Rodger")
Tommy = Dog("Tommy")

print("Rodger is a {}".format(Rodger.__class__.attr1))
print("Tommy is also a {}".format(Tommy.__class__.attr1))

print("My name is {}".format(Rodger.name))
print("My name is {}".format(Tommy.name))


