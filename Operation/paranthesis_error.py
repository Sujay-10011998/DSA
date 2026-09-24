import traceback

def add_element_at_any_position(arr, element, position):
    if position < 0:
        position = 0
    elif position > len(arr):
        position = len(arr)
    arr.insert(position, element)
    return arr

try:
    # Take array from user input
    my_array = input("Enter elements of the array separated by spaces: ").split()
    my_array = [int(x) for x in my_array]  # Convert elements to integers

    # Take element and position from user input
    new_element = int(input("Enter the element you want to add: "))
    desired_position = int(input("Enter the position where you want to add the element: "))

    result = add_element_at_any_position(my_array, new_element, desired_position)
    print("Updated array:", result)

except SyntaxError as e:
    print("Syntax error found on line:", traceback.extract_tb(e.__traceback__)[0].lineno)
