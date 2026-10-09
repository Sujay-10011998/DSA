def two_sum(arr, target):
    l = len(arr)
    for i in range(l):
        for j in range(i+1, l):
            if arr[i] + arr[j] == target:
                return i, j
            
u = list(map(int, input("Enter arr elements separated by space: ").split()))
t = int(input("Enter target: "))
l = two_sum(u, t)

if l:
    print("the indexes are: ", l)


#using enumerate

