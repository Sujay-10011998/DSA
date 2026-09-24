#new_set = {expression for item in iterable if condition}
squares = {x**2 for x in range(0, 5)}
print(squares)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = {x for x in numbers if x % 2 == 0}
print(even_numbers)
