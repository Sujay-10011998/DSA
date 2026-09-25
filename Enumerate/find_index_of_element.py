def find_index_of_element(arr, value):
    if value not in arr:
        print(f"The {value} is not present in the array")

    for i, j in enumerate(arr):
        if j == value:
            return i

l = list(map(int, input("Enter arr elements separated by space: ").split()))
d = int(input("Enter the value: "))
k = find_index_of_element(l,d)
if k:
    print(f"index of {d} is {k}")