def find_max(arr):
    max = 0
    
    for i in arr:
        if i > max:
            max = i

    return max


array = list(map(int,input("Enter arr elements: ").split()))   

res = find_max(array)

if res:
    print(f"found max no: ", res)
else:
    print(f"error")