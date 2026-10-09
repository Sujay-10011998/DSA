def product_of_elements_except_self(arr):
    l = len(arr)
    result = []

    for i in range(l):
        pro = 1
        for j in range(l):
            if i != j:
                pro = pro * arr[j]
        result.append(pro)
    return result


arr = [1, 2, 3, 4]
print(product_of_elements_except_self(arr))