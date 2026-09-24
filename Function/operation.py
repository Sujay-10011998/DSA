#map
def square(x):
    return x * x

numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(square, numbers))
print(squared_numbers)  


#lambda: Lambda functions (also known as anonymous functions) are small, unnamed functions defined using the lambda keyword.
#They can take any number of arguments but can only have one expression

square = lambda x: x * x             #(arguments: expression)
print(square(4)) 

#lambda using map
list1 = [12,34,75,89,21]
res1 = list(map(lambda m: m**2, list1))
print(res1)

#lambda using filter
a = [78,34,798,23,9876]
res2 = list(filter(lambda g: g%2==0, a))
print(res2)

#recursion
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


