#short-circuiting refers to the behavior of logical operators (and and or) where the second operand is evaluated only if the first operand doesn't determine the outcome.

a = False
b = True
result = a and b  # Since 'a' is False, 'b' is not evaluated, result is False

a = True
b = False
result = a or b  # Since 'a' is True, 'b' is not evaluated, result is True
