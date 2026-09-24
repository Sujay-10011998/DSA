import traceback

def example_function():
    # Some code that may raise an exception
    try:
        result = 1 / 0  # This will raise a ZeroDivisionError
    except Exception as e:
        # Use traceback to print the stack trace
        traceback.print_exc()

# Call the example function
example_function()
