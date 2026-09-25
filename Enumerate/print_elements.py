def printEnu(arr):
    for i, j in enumerate(arr):
        print(i,j)

l = list(map(int, input("Enter arr elements separated by space: ").split()))
k = printEnu(l)
if k:
    print(f"printing elements using enumerate: {k}")