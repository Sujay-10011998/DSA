def three_sum(arr):
    l = len(arr)
    res=[]
    for x in range(l):
        for y in range(x+1, l):
            for z in range(y+1, l):
                if arr[x] + arr[y] + arr[z] == 0:
                    res.append([arr[x], arr[y], arr[z]])
                    
    return res

arr = list(map(int, input("Enter array elements separated by spaces").split()))

k = three_sum(arr)

print("The elements sum up to 0 are:", k)
