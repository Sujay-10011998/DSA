def find_min(arr):
    min = arr[0]
    
    for i in arr:
        if i < min:
            min = i
            
    return min

arr = list(map(int, input("arr elements: ").split()))
res = find_min(arr)
print(res)