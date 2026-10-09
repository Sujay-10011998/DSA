def contains_duplicate(arr):
    seen = []
    dup = []

    for i in range(len(arr)):
        if arr[i] in seen:
            dup.append(arr[i])
        else:
            seen.append(arr[i])

    return dup


f = list(map(int, input("enter arr elements separated by space: ").split()))

res = contains_duplicate(f)
print(f"duplicate elements: {res}")