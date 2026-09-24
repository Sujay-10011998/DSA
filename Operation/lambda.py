#lambda arguments: expression

add = lambda x, y: x + y
result = add(3, 5)
print(result)  


numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, numbers))
print(squared)  # Output: [1, 4, 9, 16, 25]

