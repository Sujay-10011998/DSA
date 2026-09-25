def x_to_y_elements(arr):
    e = arr[2:8]
    return e

r = list(map(int, input("Enter elements with space: ").split()))
p = x_to_y_elements(r)

if p:
    print(f"after slicing, the 2nd to 7th indexed elements are: {p}")