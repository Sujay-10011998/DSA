# *args is used in a function definition to allow the function to accept a variable number of positional arguments
#When you prefix a parameter with an asterisk (*) in a function definition,
# it allows the function to accept any number of positional arguments.
def A(*args):
    for i in args:
        print(i, end=",")

A(12,34,65,2)    


# **kwargs is used in a function definition to allow the function to accept a variable number of keyword arguments.
# When you prefix a parameter with two asterisks (**) in a function definition,
# it allows the function to accept any number of keyword arguments.

def B(**kwargs):
    for key, value in kwargs.items():
        print(key, value)

B(first_name="John", last_name="Doe", age=30)
