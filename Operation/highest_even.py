#max even element
def find_h_even(li):
    h_even = None
    for i in li:
        if i%2==0:
            if h_even is None or i>=h_even:
                h_even = i
    return h_even    

list = [21,54,2,12,367,222]
result = find_h_even(list)
if result is not None:
    print("highest even no is : " + str(result))
else:
    print("there is no even no")    
    
    
    
#max element 
def find_high(lst):
    h = None
    for j in lst:
        if h is None or j>=h:
            h = j
    return h
lst2 = [21,54,2,12,367,222]
res = find_high(lst2)
if res is not None:
    print("highest no is : " + str(res))
else:
    print("there is no highest no") 