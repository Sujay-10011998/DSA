def some_function():
    print("Function in example_module")

if __name__ == "__main__":
    print("This script is being run as the main program")
    some_function()
else:
    print("This script is being imported as a module")
