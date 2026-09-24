#local scope
def my_function():
    x = 10  # This variable x has a local scope and is accessible only within my_function.
    print(x)

my_function()  # Output: 10
print(x)  # This will raise a NameError because x is not defined in this scope.

#enclosing scope
#This scope is applicable for nested functions. 
# If a variable is not found in the local scope of a function, Python will search in the enclosing scopes.
def outer_function():
    y = 20  # This variable y is in the local scope of outer_function

    def inner_function():
        print(y)  # y is in the enclosing scope of inner_function

    inner_function()

outer_function()  # Output: 20



#Global scope: A variable is in the global scope if it is declared outside of any function.
# It can be accessed from any part of the program.
z = 30  # This variable z is in the global scope

def my_function():
    print(z)  # z is in the global scope and can be accessed inside the function

my_function()  # Output: 30


#Built-in scope: 
# Python also has a built-in scope that contains names such as keywords and built-in functions like print(), len(), etc
print(len("hello"))  # Output: 5
