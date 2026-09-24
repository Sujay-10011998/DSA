def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i  # Return the index of the found element
    return -1  # If element is not found, return -1

# Take user input
arr_input = input("Enter the elements of the array separated by spaces: ")
arr = list(map(int, arr_input.split()))  # Convert the input string to a list of integers

target = int(input("Enter the target value: "))

# Call the linear search function and print the result
result = linear_search(arr, target)
print(f"The target value {target} is at index: {result}")
