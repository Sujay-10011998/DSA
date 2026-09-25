def find_all_indices_where_value_occurs(arr, value):
    ind = []

    for f, m in enumerate(arr):
        if m == value:
            ind.append(f)
    return ind

l = list(map(int, input("Enter arr elements separated by space: ").split()))
o = int(input("Enter value: "))
k = find_all_indices_where_value_occurs(l,o)
if k:
    print(f"Printing the indexes {k} of the value {o}")