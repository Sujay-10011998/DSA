def get_first_3_elements(arr):
    o = arr[:3]     #for last 3 elements arr[3:]
    
    return o

r = list(map(int, input("Enter array elements: ").split()))

d = get_first_3_elements(r)
if d:
    print(f"array after slicing: {d}")





