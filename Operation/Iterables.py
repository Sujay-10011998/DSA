#In Python, an iterable is an object capable of returning its elements one at a time. 
# This includes sequences (like lists, tuples, and strings), collections (like sets and dictionaries), and other iterable objects.
# Iterables are fundamental in Python, as they allow you to loop through elements efficiently without having to know how the iteration is implemented internally.


#iterate through values using the yield keyword
def my_generator():
    yield 1
    yield 2
    yield 3

for num in my_generator():
    print(num)
