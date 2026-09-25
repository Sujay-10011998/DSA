def odd_indexed(arr):
    y = arr[1::2]
    return y

u = list(map(int, input("Enter arr elements separated by space: ").split()))
l = odd_indexed(u)
if l:
    print(f"Odd indexed elements: {l}")