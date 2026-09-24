def sum(x,y):
    sum = x+y
    return sum
result = sum(10,20)
print(result)


# Function without parameters
def greet():
    print("Hello, world!")

greet() 

# Function with default parameter value
def greet_person(name="Guest"):
    print("Hello, " + name + "!")

greet_person()         
greet_person("Corporate")  
