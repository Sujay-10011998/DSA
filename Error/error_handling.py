try:
    result = 10 / 0
except ZeroDivisionError:
    print("Error: Division by zero is not possible!")
except Exception as e:
    print(f"An error occurred: {e}")
else:
    print("Division successful!")
finally:
    print("This will always execute, regardless of an exception.")


list = [21,43,35,84]
try:
    res = print(list[100])
except IndexError:
    print("100 is greater than length of list")
except Exception as e:
    print("error found!")
    
finally:
    print(res)         #finally executes -NameError: name 'res' is not defined