# Without the walrus operator
x = 10
if x > 5:
    print("x is greater than 5")
else:
    print("x is not greater than 5")

# With the walrus operator
y = 10
if (z := y) > 5:
    print("z is greater than 5")
else:
    print("z is not greater than 5")
