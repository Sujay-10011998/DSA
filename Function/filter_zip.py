#The filter() function in Python is used to filter elements of an iterable (like a list, tuple, or set) based on a given function

lt = [21,42,1,4,65,7656]
def even(num):
    return num%2==0

res  = (list(filter(even, lt)))
print (res)


#The zip() function in Python is used to combine two or more iterables 

li = [21,45,0,90,3]
lis = ["sujay","mondal"]

res = list(zip(li,lis))
print(res)