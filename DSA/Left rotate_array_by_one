def rotate_arr_by_one(arr):
    
    l = len(arr)
    last = arr[l-1]
    
    for i in range(l-1, 0, -1):
        arr[i] = arr[i-1]
    
    arr[0] = last
    
    return arr
    
d = list(map(int, input("Enter array elements separated by space: ").split()))
x = rotate_arr_by_one(d)

print(f"the rotated array is{x}")